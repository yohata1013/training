import re

mail = 'yohata1013@gmail.com'
r = re.compile(r'(.+[a-z]).+[0-9]@.+')
m=r.search(mail)

if m:
    target = m.group(1)

    print(target)
