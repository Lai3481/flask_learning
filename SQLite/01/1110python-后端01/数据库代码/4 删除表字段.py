import sqlite3 

conn = sqlite3.connect("test.db")


yb = conn.cursor()
yb.execute("drop table teacher;")
#drop 用于删除字段 
# delete 用于删除表记录

conn.commit()

yb.close()
conn.close()