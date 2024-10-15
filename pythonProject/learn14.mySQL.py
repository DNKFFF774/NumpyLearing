
from pymysql import Connection

conn = Connection(
     host='localhost',#主机名(ip)
     port=3306,         #端口
     user='root',
     password='322898',
    autocommit=True
 )
print(conn.get_server_info())

cursor = conn.cursor()
conn.select_db("world")#等于use数据库

# cursor.execute("CREATE TABLE test_pymysql(id int,info varchar(20));")
# cursor.execute("select * from stu ")
# result = cursor.fetchall()
# print(result)
# for i in result:
#     print(i)
cursor.execute("insert into stu (id,name,age) values (7,'王',100);")
# conn.commit()#更改表格数据需要确认

conn.close()
