#yに西暦を入力
y=1900

if y%400==0:
    print("うるう年ですん")
elif y%100==0:
    print("平年ですん")
elif y%4==0:
    print("うるう年ですん")
else:
    print("平年ですん")
