# Complete the closestNumbers function below.
def closestNumbers(arr):
    # 隣同士の差が最小
    # 隣同士の差が最小であることを判断するために、すべての要素がソートされている必要がある
    # その上で、それぞれのペアがどれくらいの差を持つのかを調べていくついでに、その情報を次位書に保存していく
    # 最後に、最小の差を持つペアを取り出して返す
    # 例：[2,7,9,10,15]
    arr.sort()
    difdic = {}
    for i in range(0,len(arr)-1):
        diff = arr[i+1]-arr[i]
        if diff in difdic.keys():
            difdic[diff].append(arr[i])
            difdic[diff].append(arr[i+1])
        else:
            difdic[diff] = [arr[i],arr[i+1]]
    #最小の差を求める
    min_diff = min(difdic.keys())
    return difdic[min_diff]