import csv

with open('sample0728_aomori.csv',encoding='utf-8') as fh:
    lines = fh.readlines() # すべて読み込む
    lines = csv.reader(lines)
    next(lines) # １行目スキップ
    lines = list(lines)

    #一度平均点を出して、それを各リストの末尾に追加してあげて
    #それをもとに、並び替えをするといいのでは？
    for row in lines:
        #平均出す
        mean = (int(row[3])+int(row[4])+int(row[5]))/3
        row.append(mean) # １列追加

    lines.sort(key=lambda x:x[6], reverse=True)
    print(lines[6])
