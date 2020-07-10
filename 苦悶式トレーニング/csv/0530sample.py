import csv
with open('sample.csv',encoding='utf-8') as fh\
    , open('sample_out.csv','w',encoding='utf-8') as fh_out:

    #CSVモジュール利用準備
    reader = csv.reader(fh)
    writer = csv.writer(fh_out)

    for index,row in enumerate(reader):
        if index == 0:
            name = row[0] #田中さん入れる
        elif row[0] == '':
            row[0] = name
        elif row[0] != name:
            name = row[0]

        writer.writerow(row)
