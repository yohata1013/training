import csv
with open('sample0728_aomori.csv') as fh:
    lines = fh.readlines() # ファイルからすべてを読み込んで、改行をキーとして各行をリストに入れる
    lines = csv.reader(lines) # readerオブジェクトが入る
    next(lines) # 1行スキップ
    lines = list(lines) #readerオブジェクトはlistにキャストできる
    print(lines)

    # 出来上がったlinesについて、処理を行い、平均点順に並べて表示する