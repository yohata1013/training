import re
import csv

r=re.compile(r"^[a-zA-Z\s.]+[0-9]{5}$")

with open('testdata0627_3.csv') as fh:
    reader = csv.reader(fh)
    next(reader)


    #LastName以降の数字5桁を抽出する
    #リストの中から先頭のもの(id)を取り出す
    for row in reader:
        #idを取り出して正規表現にマッチしているか
        m=r.search(row[0])
        #マッチしていなかったらエラー
        if not m:
            print(row)
