#sample0606_1.csvを読み込んで、lastdate,exprice, name,pointという並びのCSVを作成
#expireはlastdateから30日後

import datetime
import csv

with open('sample0606_1.csv') as fh, open('sample0606_1_out.csv','w') as fh_out:
    reader = csv.reader(fh)
    writer = csv.writer(fh_out)

    #ヘッダーのカラム名を入れて、書き出す
    header = ['lastdate', 'expire', 'name', 'point']
    writer.writerow(header)

    #forで回す前に、最初の1行だけは取り出しておく
    next(reader)

    for row in reader:
        #この時点でのrowの中身はrow[0]
        #これに期限の日付、expireを追加したい

        #expireの計算
        #row[0]の中身を日付型に変更する
        lastdate_d = datetime.datetime.strptime(row[0], '%Y-%m-%d')

        #30日を足してexpireを作成する
        expire_d = lastdate_d + datetime.timedelta(days=30)
        #書き出すために、expire_dを日付型から文字列型に変換する
        expire_str = expire_d.strftime('%Y-%m-%d')
        #書き出すリストを作成
        new_list = [row[0], expire_str, row[1], row[2]]
        writer.writerow(new_list)
