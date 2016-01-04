import mysql.connector 

conn = mysql.connector.connect(user='root', password='password', database='test')


cursor = conn.cursor()
cursor.execute('drop table if exists people')
cursor.execute('create table people (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into people (id, name) values (\'1\', \'Tmac\')')
print cursor.rowcount
conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from people where id = 1' )
value = cursor.fetchall()
print value
cursor.close()


#conn.commit()
conn.close()

