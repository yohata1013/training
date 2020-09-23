import time

def extraLongFactorials(n):
    # write your code
    retval = n
    #第3引数はステップ数(今回は-1ずつしていく)
    for i in range(n-1,0,-1):
        retval *= i
    #forの結果を返すから、returnはここ！
    return retval


start = time.time()
print(extraLongFactorials(5))
end = time.time()
print(end-start)
