import re
import csv

def get_num(s): #sは文字列ではなくリストだよん
    r=re.compile(r'(\d+)')
    tmp_list=r.split(s[0])
    digit = int(tmp_list[1]) #数値に変換する
    return digit


with open('sampledata0720.csv', encoding='utf-8') as fh, open('sampledata0720_out.csv', 'w', encoding='utf-8') as fh_out:
    reader = csv.reader(fh)
    writer = csv.writer(fh_out)
    writer.writerow(next(reader)) #reader側の1行を読み込んで書き出す

    tmplist=[]

    for row in reader:
        tmplist.append(row)
    reslist = sorted(tmplist, key=get_num)

    writer.writerows(reslist) #複数の行を書く(rowsだからね)
