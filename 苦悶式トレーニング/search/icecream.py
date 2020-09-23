def icecreamParlor(m,arr):
    #足してmになればOK→全探索する
    #6の右隣は存在しないので-1にする(外側)
    for i in range(0,len(arr)-1):
        #内側。開始位置もiの値で変化する
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==m:
                return [i+1,j+1]


m = 6
cost = [1,3,4,5,6]

retvalue = icecreamParlor(m,cost)
print("%d %d"%(retvalue[0],retvalue[1]))
