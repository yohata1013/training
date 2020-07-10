import csv
with open('sample.csv', encoding='utf-8') as fh\
    ,open('sample_out2.csv', 'w',encoding='shift-jis') as fh_out:

    reader = csv.reader(fh)
    writer = csv.writer(fh_out)

    writer.writerow(['名前','国語','算数','英語','社会'])

    c=0
    writelist=[] #1行ずつデータをためて、4行ごとリストを書き出す
    for row in reader:
        if c==0:
            writelist.append(row[0]) #名前
        writelist.append(row[1]) #順番に点数を追加

        #1個人の全書けたらwriteの処理をする
        if c==3:
            writer.writerow(writelist)
            writelist=[]
            c=0
        else:
            c += 1
