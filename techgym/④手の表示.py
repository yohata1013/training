import random

def start_message():
    print('じゃんけんスタート')
    print('あなたの手を入力してください')

#自分の手を処理
def get_my_hand():
    return int(input('0:グー, 1:チョキ, 2:パー'))
my_hand = get_my_hand()

def my_handres(my_hand):
    if my_hand == 0:
        print ('君はグー')
    elif my_hand == 1:
        print ('君はチョキ')
    elif my_hand == 2:
        print ('君はパー')
    else:
        print ('君は不正な手だよ')

#相手の手を処理
def get_you_hand():
    return random.randint(0, 2)
you_hand = get_you_hand()

def you_handres(you_hand):
    if you_hand == 0:
        print ('相手はグー')
    elif you_hand == 1:
        print ('相手はチョキ')
    elif you_hand == 2:
        print ('相手はパー')
    else:
        print ('相手は不正な手だよ')

#結果の判定
def view_result(hand_diff):
    if hand_diff == 0:
        print('あいこ')
    elif hand_diff == -1 or hand_diff == 2:
        print('君の勝ち')
    else:
        print('君の負け')



my_handres(my_hand)
you_handres(you_hand)

hand_diff = my_hand - you_hand
view_result(hand_diff)
