#月ごとの平均売上を算出する
import datetime
#文字型をdatetime型に変換したい場合は、
#d=datetime.datetime.strptime('2020-01-01,'%Y-%m-%d)のように入力する。
#datetime型にすることで日付の計算をすることができる
from dateutil.relativedelta import relativedelta
import csv

with open ('20200606_sample2.csv') as fh:
    reader=csv.reader(fh)
    #1行スキップ
    next(reader)

    #繰り返すことで、リストの中に突っ込む(CSVなのでリストの中にリストが入る)
    datalist=[]
    for row in reader:
        #日付の文字列は、日付データに変換して保存する。
        d = datetime.datetime.strptime(row[0],'%Y-%m-%d')
        row[0] = d
        #日付型変換後のrowを書き込む
        datalist.append(row)

    #2018年1月～2020年12月まで繰り返す
    for year in range(2018,2021):
        for month in range(1,13):
            #数字からdatetime型を作成する
            #今回はyear年month月1日のdatetime型のデータ。
            startdate = datetime.datetime(year, month, 1)
            #各月の1日から1日を引いて、各月の月末日を把握する。
            enddate = startdate + relativedelta(months=1) - relativedelta(days=1)

            total=0
            datacounter=0

            for data in datalist:
                #dataがstartdateとenddateの間に含まれるかを判断する。
                #pythonは不等号を重ねされる
                if startdate <= data[0] <= enddate:
                    total += int(data[2])
                    datacounter += 1
            avg = total / datacounter

            writestr = "%d年%d月の平均売上は%.1fです"%(year,month,avg)
            print(writestr)
