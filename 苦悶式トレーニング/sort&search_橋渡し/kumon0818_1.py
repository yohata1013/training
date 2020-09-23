import csv

def mean(a_list):
    mean_ = (int(a_list[3]) + int(a_list[4]) + int(a_list[5]))/3
    return mean_

with open('sample0728_aomori.csv') as fh:
    lines = fh.readlines() # すべて読み込む
    lines = csv.reader(lines)
    next(lines) # １行目スキップ
    lines = list(lines)
    
    # やり方1 
    # # 一度平均点を出して、それを各リストの末尾に追加してあげて
    # # それをもとに、並び替えをするといいのでは？
    # for row in lines:
    #     # 平均出す
    #     mean = (int(row[3])+int(row[4])+int(row[5]))/3
    #     row.append(mean) # １列追加
    
    # lines.sort(key=lambda x:x[6], reverse=True)
    
    # やり方２
    lines.sort(key=mean,reverse=True)

    print(lines[:10])

