#日付を扱うのに必須のモジュール
import datetime

#今日の日付を取得する
d =datetime.date.today()

#文字列から任意の日付型のデータを作成したい
#strptime：date型のクラスにしかない、date型を文字列に変換する関数。
d=datetime.datetime.strptime('2020-06-06','%Y-%m-%d')

#3日後は？？の計算
d = d + datetime.timedelta(days=3)

#1か月足したい、はできない
#datetimeに年月を加算できるようにしたい→dateutilを追加する
