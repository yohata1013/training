from score import score
from score import extendscore
#from A import B [AのファイルからBをインポートしろ]

tanaka = extendscore()
#をつけるとクラスとして認識する
tanaka.name = "田中さん"
#「.」により、クラス内の変数に代入する
tanaka.math = 30
tanaka.english=55
tanaka.science=80
avg = tanaka.avg()
print(avg)
print(tanaka.get_name())


suzuki = score()
#をつけるとクラスとして認識する
suzuki.name = "鈴木さん"
#「.」により、クラス内の変数に代入する
suzuki.math = 40
suzuki.english=50
suzuki.science=60
avg = suzuki.avg()
print(avg)
