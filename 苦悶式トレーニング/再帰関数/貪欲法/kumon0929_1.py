# Complete the toys function below.
def maximumToys(prices, k):
    #安いのから買ってあげて、カウントアップすれば良い
    #おもちゃを金額順に並び替える
    prices.sort()
    counter=0
    total=0 #totalがkを超えなければOK。予算オーバーまでカウント。

    #予算オーバーになるまで繰り返す
    for price in prices:
        if total + price <= k:
            total += price
            counter += 1
    return counter

#TestCase should return 4
k = 50
prices = [1,12,5,111,200,1000,10] # [1, 5, 10, 12, 111, 200, 1000]


print(maximumToys(prices,k))
