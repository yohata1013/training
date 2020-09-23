import time

def extraLongFactorials(n):
    # write your code
    if n==1:
        return 1
    else:
        return n * extraLongFactorials(n-1)

start = time.time()
print(extraLongFactorials(5))
end = time.time()
print(end-start)
