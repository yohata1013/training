#枚数は気にしない。払えること前提。
coins=[1,5,10,50,100,500]

#引数a=ターゲットの金額
def countcoins(a):
    #sort()のデフォルトは小さい順(昇順)。reverse1を入れると降順
    coins.sort(reverse=True)
    count=0

    #コインを1枚ずつ取り出す
    for coin in coins:
        div = int(a/coin)
        count += div
        a -= coin*div
    return count

#テストケース
a=620
print(countcoins(a))
