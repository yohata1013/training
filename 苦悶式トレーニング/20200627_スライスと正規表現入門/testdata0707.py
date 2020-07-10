import re
import csv

#チェック用パターンと修正用パターンを作成する
#チェック用
r_checker = re.compile(r'^[0-9]+-[0-9]+$')
#修正用
r_modifier = re.compile(r'^([0-9]{3})([0-9]{4})$')

with open ('testdata0707.csv',encoding='utf-8') as fh\
    , open('testdata0707_rev.csv','w',encoding='utf-8') as fh_out:
    reader=csv.reader(fh)
    writer=csv.writer(fh_out)
     #1行目書き出し
    writer.writerow(next(reader))

    for row in reader:
        m=r_checker.search(row[7])
        #mがnullならエラー、だからハイフンをつける

        if not m:
            #修正対応
            m_mod=r_modifier.search(row[7])
            #r_modifier内の()の前半(3桁)
            first=m_mod.group(1)
            #r_modifier内の()の前半(4桁)
            second=m_mod.group(2)
            #修正された郵便番号
            writestr=first+'-'+second

        writer.writerow(row)
