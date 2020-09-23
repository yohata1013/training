a = [('abc',2),('def',5),('efg',1),('hij',4),('klm',3)]
#ソートキーをlambdaでセット
b = sorted(a,key=lambda x:x[1])

print(b)
