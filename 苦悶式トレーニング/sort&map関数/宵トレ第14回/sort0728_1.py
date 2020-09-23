import csv
with open('sample0728_aomori.csv') as fh:
    reader = csv.reader(fh)
    next(reader) #1行目スキップ
    scorelist = []
    for row in reader:
        scorelist.append(int(row[3])) # 取り込む際に文字列から整数にキャストしておく
    
    #並び替える
    scorelist.sort()
    
    #中央値を求める
    if len(scorelist)%2==0: # 要素は偶数個
        latter_index = int(len(scorelist)/2) # 割り算したものは小数の型として返ってくるので、整数に変換
        latter = scorelist[latter_index] # 後ろの方の数値
        former_index = latter_index - 1
        former = scorelist[former_index] # 前側の数値
        median = (former + latter) / 2
    else:                   # 要素は奇数個
        middle_index = int(len(scorelist)/2) # 中央のインデックス
        median = scorelist[middle_index]
    
    print(median)