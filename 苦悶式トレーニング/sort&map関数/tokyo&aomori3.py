import csv,re
import datetime

with open('sample0728_tokyo.csv', encoding='utf-8') as fh:
    englist=[]
    reader = csv.reader(fh)
    next(reader)

    #条件を満たす人だけを抽出する
    #正規表現
    r=re.compile(r'([0-9]{4})/')

    for row in reader:
        birth=row[2]
        m=r.search(birth) #マッチしたら抽出し、mに入る
        #今回は確実には入っている前提
        birthyear=int(m.group(1))

        #対象期間の人だけのデータを使用する
        if 1985 <= birthyear <= 1990:
            englist.append(row) #とりま全部


    #トップ10を抽出する※英語の点数だけ
    #いつもの
    #e_score=[]
    #for row in englist:
    #    e_score.append(row[5])

    #map関数を使おう
    e_score=list(map(lambda x:x[5],englist))

    #10番目の数字が何かチェックする→重複を避けて10番目を取る
    #重複削除→set
    e_score=list(set(e_score)) #一度set(集合)にキャストしてlistに戻す
    #並び替え(TOP10を出す)
    e_score.sort(reverse=True)
    top10 = int(e_score[9])

    #10番目の値以上の人たちを抽出
    reslist=[]
    for item in englist:
        if int(item[5])>=top10:
            reslist.append([item[0],int(item[5])])

    #最後にソートして出力
    reslist.sort(key=lambda x:x[1],reverse=True)
    for item in reslist:
        print("%s %d"%(item[0],item[1]))
