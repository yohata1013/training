import csv

with open('testdata0627.csv') as fh:
    reader= csv.reader(fh)
    #ヘッダーをスキップ
    next(reader)

#ミスのある行を表示すればOK
    for s in reader:
        #IDの項目だけを取得してチェックする(5桁か否か)
        if len(s[0])!=5:
            print(s)
