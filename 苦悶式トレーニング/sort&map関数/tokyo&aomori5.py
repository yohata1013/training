import csv

#a_listはこれから読み込むリストのための仮置き
def mean(a_list):
    mean_=(int(a_list[3])+int(a_list[4])+int(a_list[5]))/3
    return mean_

with open('sample0728_aomori.csv',encoding='utf-8') as fh:
    lines = fh.readlines() # すべて読み込む
    lines = csv.reader(lines)
    next(lines) # １行目スキップ
    lines = list(lines)

    lines.sort(key=mean,reverse=True)
    print(lines[:10])
