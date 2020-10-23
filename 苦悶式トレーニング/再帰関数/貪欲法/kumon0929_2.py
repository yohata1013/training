# Complete the toys function below.
def toys(w):
    #主さの小さい順に並び替え
    #重複があったとしても意味がない
    w=sorted(list(set(w)))
    counter=1 #必ずコンテナを1つは利用する。→1スタート
    #+4の値を計算しておく必要がある
    an=w[0]+4 #最小から4ユニット足した

    for i in range(1,len(w)):
        #+4ユニットの値(例：最小が1なら5、越えたら次のコンテナ用意)
        if w[i]>an:
            counter+=1
            #次のコンテナの最小の値を設定する
            an=w[i]+4
    return counter

# TestCase1 should return 2
w = [1,2,3,4,5,10,11,12,13]

# TestCase2 should return 4     [1, 2, 3, 7, 12, 14, 21, 21]
#w = [1,2,3,21,7,12,14,21]

print(toys(w))
