a="パトカー"
b="タクシー"
ans=""

#zipで短い方に合わせて1文字ずつ取り出す
for i,j  in zip(a,b):
    ans += i+j

print(ans)
