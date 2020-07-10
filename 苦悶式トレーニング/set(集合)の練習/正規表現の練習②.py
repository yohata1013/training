import csv
import re

r = re.compile('^https?://([^/]+).*$')

with open('testdata0620.csv') as fh, open('testdata0620_out.csv','w') as fh_out:
  reader = csv.reader(fh)
  next(reader)#1行目スキップ

  #書き出し用
  writer = csv.writer(fh_out)

  #空の集合を作って、順番にドメインを追加していく
  unique_domain_set=set()
  for row in reader:
      #ドメインを抽出する
      domain = r.search(row[1]).group(1)
      #1つ目が日付、2つ目がドメインのため
      unique_domain_set.add(domain)

  print(unique_domain_set)
  print(len(unique_domain_set))#要素がいくつあるか

  for domain in unique_domain_set:
      writer.writerow([domain])#リストにして渡す
