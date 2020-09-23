import re

#テストしたい正規表現を入れる
#\を使うと直後に来たものは正規表現ではなく、元々の意味になる
r = re.compile(r'^\S+@[^-.]+.*[^-.]+\.[a-z]+$')

while(True):
    testtext = input()

    if testtext == 'end':
        break
    m=r.search(testtext)

    if m:
        print("yes")
        break
    else:
        print("no")
        break
