import csv

with open('testdata0627_2.csv') as fh:
    reader = csv.reader(fh)
    next(reader)

    for row in reader:
        id = row[0]
        #先頭がIDかどうかを確認する
        head = id[:2]
        if head != 'ID':
            print(row)
            continue #この時点で処理を切り上げてfor文の先頭に戻る

        #ID以下の桁数が5桁かどうか
        num=id[2:]
        if len(num)!=5:
            print(row)
