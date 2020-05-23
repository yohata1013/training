import MySQLdb;

conn = MySQLdb.connect(host='localhost', user='root', passwd='mysql', db='testdb2')

cursor=conn.cursor()

with open('20200331data1.txt',encoding="utf-8") as fh:
    for line in fh:
        line = line.rstrip()
        items= line.split(',')
        sql = "insert into testtable(name,area,english,math,science) values ('%s', '%s', %s, %s, %s)" %(items[0],items[1], items[2], items[3],items[4])
        cursor.execute(sql)
conn.commit()
conn.close()
