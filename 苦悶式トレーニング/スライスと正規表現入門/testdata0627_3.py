import re
import csv

with open('testdata0627_3.csv') as fh:
    reader = csv.reader(fh)
    next(reader)


    #LastName以降の数字5桁を抽出する
    #リストの中から先頭のもの(id)を取り出す
    for row in reader:
        id = row[0]

        #idからlastnameを抽出する
        r = re.compile(r'.+[a-z](.+[0-9])')
        m=r.search(id)

        #group()に番号を入れることで()内を取り出す
        #内の番号は()で何番目かを記入する
        #今回はrのうち1番目だし、それしかない。
        target=m.group(1)

        if len(target) != 5:
            print(row)
