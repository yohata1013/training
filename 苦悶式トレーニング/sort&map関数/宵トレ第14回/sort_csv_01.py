import csv,re
def get_numbers(s): # 引数として渡されるのは文字列ではなくリスト
    r = re.compile(r'(\d+)') 
    tmp_list = r.split(s[0])  # 例： ID55 -> ['ID','55']
    digit = int(tmp_list[1])
    return digit

with open('sampledata0720.csv') as fh, open('sampledata0720_sorted.csv','w') as fh_out:
    reader = csv.reader(fh)
    writer = csv.writer(fh_out)
    writer.writerow(next(reader)) # 1行目のヘッダを読み込んで、書き出しておく
    # 扱いやすいように一度データを読み込んで、リストに保存しておく
    tmplist = []
    for row in reader:
        tmplist.append(row)
    resultlist = sorted(tmplist,key=get_numbers)

    writer.writerows(resultlist)

    