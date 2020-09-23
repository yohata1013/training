#考え方：東京・青森それぞれで中央値を出して、2で割って小数点を切り捨てれば中央値になる！！

import csv

with open('sample0728_tokyo.csv', encoding='utf-8') as fh:
    reader = csv.reader(fh)
    next(reader) #ヘッダー不要なので1行目スキップ

    #とにかく中央値～～～～
    scorelist=[]

    for row in reader:
        scorelist.append([row[0],int(row[4])]) #取り込む際に数字にキャストしておく

    #並び変える
    scorelist.sort(key=lambda x:x[1])

    #中央値を求める
    #要素が偶数→中央値がお尻に来る
    if len(scorelist)%2==0:
        last_index =  int(len(scorelist)/2)
        last = scorelist[last_index]
        fw_index = last_index - 1
        former = scorelist[fw_index]
        med = (former[1] + last[1]) / 2
        writestr = "中央値の人は %sと%s, 中央値は %.02f"%(former[0],last[0],med)    #要素が奇数
    else:
        mid_index = int(len(scorelist)/2)
        med = scorelist[mid_index][1]
        name = scorelist[mid_index][0]
        writestr = "中央値の人は %s %s, 中央値は %.02f"%(name,med)

    print(writestr)
