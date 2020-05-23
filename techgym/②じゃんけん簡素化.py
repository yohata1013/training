import random

print('じゃんけんスタート')

print('あなたの手を入力してください')
my_hand = int(input('0:グー, 1:チョキ, 2:パー'))
you_hand = random.randint(0, 2)

#差分を出す
d=my_hand-you_hand

if d=0:
  print("あいこ")
elif d=-1 or d=2:
  print("勝ち")
else:
  print("負け")
