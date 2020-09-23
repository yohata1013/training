import re
import csv

#流れ：csv読み込み→生年月日のカラム取り出し、データを確認

with open ('testdata0707.csv',encoding='utf-8') as fh:
    #{}内に数字を入れると中の数が直前の正規表現の数になる
    r = re.compile(r'([0-9]{4})/([0-9]+)/([0-9]+)')
    reader = csv.reader(fh)
    next(reader)

    for row in reader:
        #必ずマッチするのでif文は不要
        m = r.search(row[3])

        #正規表現で取得した値は文字列
        year = m.group(1)
        month = m.group(2)
        day = m.group(3)

        #%2d→0埋めをして2桁で表してね
        month = "%02d"%int(month)
        day = "%02d"%int(day)

        date = "%s/%s/%s"%(year,month,day)
        print(date)
