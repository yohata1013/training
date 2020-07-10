a=12
b=18
k=2

if a>b:
    m=a
else:
    m=b

l=[]

for i in range(1,m+1):
    if a%i==0 and b%i==0:
        l.append(i)

print(l[k+1])
