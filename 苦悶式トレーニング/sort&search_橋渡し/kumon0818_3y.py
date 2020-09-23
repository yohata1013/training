import time
#リスト内の探索は遅い→オブジェクトだし、メモリには分散して保存されている等
#リストをそのまま探索することは推奨されない
#→集合(sei)に変換する。numpy.arrayを利用する。

#データ10万件くらい
with open('sampledata0818_2.txt') as fh:

    target=[1339,3230,7532,7586,99862,10010]
    txt=fh.read()
    tmplist=txt.split(' ') #splitは引数を区切り文字として文字列を分割する

    #要素を文字列から整数に変換する
    #別にfor文でもいいけどさ、map関数使おう
    #mapはmapで戻ってきてしまうのでlistにする
    tmplist=list(map(lambda x:int(x),tmplist))

    #リストを読み込んだ段階から処理時間の計測を開始する
    start=time.time()

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
