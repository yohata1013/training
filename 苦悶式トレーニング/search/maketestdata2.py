import random
with open('testtextdata01.txt','w') as fh:
    for i in range(0,1000000):
        tmpstr = chr(random.randint(97,122))*(random.randint(1,300))
        fh.write('%s\n'%tmpstr)
