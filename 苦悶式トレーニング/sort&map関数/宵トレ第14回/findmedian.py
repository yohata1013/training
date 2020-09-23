# Complete the findMedian function below.
def findMedian(arr):
    # なにはともあれソート
    arr.sort()
    # 中央値は要素数を2で割って切り捨て
    i = int(len(arr)/2) # 整数にキャスト
    med = arr[i]
    return med