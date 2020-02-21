import pymysql
import pymysql.cursors
#连接mysql
connection = pymysql.connect(
    host='localhost',
    user = 'root',
    password = 'toor',
    db = 'class',
    port = 3306,
    charset = 'utf8'
)
# with connection.cursor() as cursor:
#     sql_1 = 'select * from student'
#     cout_1=  cursor.execute(sql_1)
cursor = connection.cursor()
# create
DB_NAME = 'test'
cursor.execute('DROP DATABASE IF EXISTS %s' %DB_NAME)
cursor.execute('CREATE DATABASE IF NOT EXISTS %s' %DB_NAME)
connection.select_db(DB_NAME)
# create table
TABLE_NAME = 'user'
cursor.execute('CREATE TABLE %s(id int primary key,name varchar(30))' %TABLE_NAME)
# insert mounts of data
values = []
for i in range(20):
    values.append((i,'kk'+str(i)))
cursor.executemany('INSERT INTO user values(%s,%s)',values)
# select * from user
count = cursor.execute('SELECT * FROM %s'%TABLE_NAME)
print('total records:',cursor.rowcount)
# 获取表名信息
desc = cursor.description
print("%s %3s" %(desc[0][0],desc[1][0]))

cursor.scroll(10,mode='absolute')
results = cursor.fetchall()
for result in results:
    print(result)
cursor.close()
connection.close()
