import random
import csv

with open('output_0901y.txt','w') as fh_out:
    #1000万件のデータを作成する
    for i in range(10000000):
        #長さを決める
        length=random.randint(1,100)
        #長さを決めたら文字を設定して、それをlength分繋げる

        #
        addchar=chr(random.randint(97,122))
        #pythonは文字列の掛け算が可能
        tmp=addchar*length

        #30分の1の確率でappleを仕込む
        #1から30のうちの5番目に割り振られたとき
        if random.randint(1,30)==5:
            tmp+='apple'

        #ドメイン名を付与
        tmp+='@hogehoge.com'

        fh_out.write("%s\n"%tmp)
