#リストのリバースを作りたい
a_list=[1,2,3,4,5]

#愚直に
for i in range(len(a_list)-1,0,-1):
  pass

reversed=[]
for i in range(len(a_list)-1,-1,-1):
        reversed.append(a_list[i])
print(reversed)


#そんなことしなくてもPythonにはスライスって機能があるよ
a_list=[1,2,3,4,5]
#開始から終了のまでコロンで区切る
#ただし最後は含まれないため注意（例：3まで指定すると0から数えて3番目は含まれず、2番目で終了）
sliced = a_list[0:3]
print(sliced)
#スライスは省略もできるよ
#開始部分を省略→最初から
sliced = a_list[:3]
print(sliced)
#修了部分を省略→最後まで
sliced = a_list[2:]
print(sliced)
#最初も最後も省略→リスト全て
sliced = a_list[:]
print(sliced)
#コロン2つでステップ数を指定（例：2なら1つ飛ばし。1まらそのまま）
sliced = a_list[::2]
print(sliced)

#スライスを活用してリストのリバース
#ステップをマイナスにすると逆から取り出す
reversed = a_list[::-1]
print(reversed)

#文字列でもできる
a_str="abcde"
reversed_str = a_str[::-1]
print(reversed_str)


#絶対値の取得
#absっていう関数を使うよ
print(abs(-20))
print(abs(20))


#リスト同士の比較
a=[1,2,3]
b=[1,2,3]
#等しいか知るには「==」でOK
print(a==b)

#活用例
c=[1,2,4]
if a==c:
    print("等しい")
else:
    print("等しくない")


#ascii valueの出し方
#ord関数を使う
print(ord('a'))
