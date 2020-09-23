import csv
with open('sample0728_tokyo.csv') as fh:
    reader = csv.reader(fh)
    next(reader) #1行目スキップ
    scorelist = []
    for row in reader:
        scorelist.append([row[0],int(row[4])]) # 取り込む際に文字列から整数にキャストしておく
    
    #並び替える
    scorelist.sort(key=lambda x:x[1])
    
    #中央値を求める
    if len(scorelist)%2==0: # 要素は偶数個
        latter_index = int(len(scorelist)/2) # 割り算したものは小数の型として返ってくるので、整数に変換
        latter = scorelist[latter_index] # 後ろの方の数値が入ったリスト
        former_index = latter_index - 1
        former = scorelist[former_index] # 前側の数値が入ったリスト
        median = (former[1] + latter[1]) / 2
        writestr = "中央の人は %s %s, 中央値は %.02f"%(former[0],latter[0],median)
    else:                   # 要素は奇数個
        middle_index = int(len(scorelist)/2) # 中央のインデックス
        median = scorelist[middle_index][1] # 数値を取り出す
        name= scorelist[middle_index][0]
        writestr = "中央の人は %s 中央値は%d"%(name,median)
    
    print(writestr)