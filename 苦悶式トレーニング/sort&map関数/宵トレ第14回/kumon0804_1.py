import csv,re

with open('sample0728_tokyo.csv') as fh:
    scorelist = []
    reader = csv.reader(fh)
    next(reader)

    # 条件を満たす人たちだけを抽出する
    r = re.compile(r'([0-9]{4})/')
    for row in reader:
        birthday = row[2] # '2020/08/04'
        m = r.search(birthday) # matchした部分があればマッチングインスタンスがmの中に入る
        birthyear = int(m.group(1)) # group(n) で抽出された値は文字列なので、整数に変換する
        
        # birthyear = int(r.search(birthyear).group(1)) ←　1行で書いても大丈夫

        # birthyearが1985から1990の間にあれば、そのデータは使用する
        if 1985 <= birthyear <= 1990:
            scorelist.append(row)

    #TOP10を抽出する
    # 英語の点数だけをまず抽出する
    # e_score = []
    # for row in scorelist:
    #     e_score.append(row[5])
    
    # map関数を使うバージョン
    e_score = list(map(lambda x:x[5],scorelist))
    print(e_score)

    # 10番目の数字が何かをチェックする -> 重複をすべて削除した上で10番目の数字を取ればいい
    e_score = list(set(e_score)) # 一度set(集合)にキャストした上でlistに戻す
    e_score.sort(reverse=True) # top10を出すためにソート
    print(e_score)
    top10 = int(e_score[9]) # top10
    print(top10)

    # 10番目の値以上の人たちを再び抽出
    resultlist= []
    for item in scorelist:
        if int(item[5])>=top10:
            resultlist.append([item[0],int(item[5])]) # [名前,整数化した英語の点数]
    
    # 最後にもう一度ソートして出力
    resultlist.sort(key=lambda x:x[1],reverse=True)
    for item in resultlist:
        print("%s %d"%(item[0],item[1]))

