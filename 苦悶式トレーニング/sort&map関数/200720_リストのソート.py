import re

alist = ['file11.txt','file12.txt','file13.txt','file2.txt','file3.txt','file4.txt']

#リストの元々の順番
alist.sort()
print(alist)

#数字をソート出来たら良い
#文字列から数字を取り出して、数値として返す
def get_num(s):
    r=re.compile(r'(\d+)')
    tmp=r.split(s)
    digit = int(tmp[1]) #数値に変換する
    return digit

res=sorted(alist,key=get_num)
print(res)
