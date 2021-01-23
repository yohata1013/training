from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .models import Question, Choice

# 質問を取得して表示
def index(request):
    question_list = Question.objects.all()
    context = {'question_list':question_list}
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    question = Question.objects.get(id=question_id)
    context = {'question':question}
    return render(request,'polls/detail.html',context)

#vote
def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)#pkはidと同じ
    #例外処理。Tryは無事にquestion_idが取得できた時。
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        context = {'question':question, 'error_message':'選択されていません'}
        return render(request, 'polls/detail.html', context)
    else:
        #ちゃんと質問のオブジェクトも選択肢のオブジェクトも取得できたので、選択したものに1投票
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request,'polls/results.html', context)

def aggregate(request):
    #全質問を取り出す。できれば登録日順で取り出したい
    question_list = Question.objects.all().order_by('pub_date')
    aggregate_list = []
    #all_votesは全票数をカウントするためのリスト
    all_votes = 0
    #全ての選択肢の票数を数える
    total_votes = 0

    for question in question_list:
        #選択肢についている質問を全て返しいて、1番大きい票数の選択肢を判断する
        #その後、全ての選択肢の票数を数え上げていく。
        #上2つのことをFor文の中でやらせる
        choices = question.choice_set.all()
        #最も選択肢が多い選択肢と票数を保存する。Noneは空の状態。最大のものだけ残る。
        max_voted_choice = None
        max_votes = 0

        for choice in choices:
            if max_voted_choice is None or choice.votes>max_voted_choice.votes:
                max_voted_choice = choice
            total_votes += choice.votes

        aggregate_list.append({'question':question,'max_voted_choice':max_voted_choice})
        #totalを全て合計すると全選択肢の投票数になることから
        all_votes += total_votes

    context = {'aggregate_list':aggregate_list,'all_votes':all_votes}
    print(aggregate_list)
    print(all_votes)

    return render(request, 'polls/aggregate.html',context)
