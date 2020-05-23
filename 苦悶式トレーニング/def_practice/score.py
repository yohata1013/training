#Classの定義
class score():
    name = ""
    #名前なので空の文字列を指定する
    #以下、最低限の点数は不明のため0にする
    math = 0
    english = 0
    science = 0
    def avg(self):
        #selfは呼び出される自分自身→呼び出し先にselfは不要
        cavg = (self.math+self.english+self.science)/3
        return cavg

class extendscore(score):
#()内の機能を継承する.手を入れず拡張したい場合は使える。
    def get_name(self):
        return self.name + "さん"
