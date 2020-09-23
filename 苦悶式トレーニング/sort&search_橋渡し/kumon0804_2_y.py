import time

with open('sampledata0818_1.txt') as fh:
    start=time.time()
    target=[13,30,753,7586,9999]
    #1行しかないのでこれでOK
    txt=fh.read()
    tmplist=txt.split(' ') #splitは引数を区切り文字として文字列を分割する

    #要素を文字列から整数に変換する
    #別にfor文でもいいけどさ、map関数使おう
    #mapはmapで戻ってきてしまうのでlistにする
    tmplist=list(map(lambda x:int(x),tmplist))

    for t_value in target:
        #targetがtmpに入っているか
        if  t_value in tmplist:
            #存在するなら値＋yes
            print("値 %d Yes"%t_value)
        else:
            print("値 %d No"%t_value)
    end=time.time()
    diff=end-start
    print(diff)
