import sqlite3

conn = sqlite3.connect("test.db")


# 修改表名语法
#      alter table 旧表名 rename to 新表名;
sql = "alter table teacher rename to teachers;"


yb = conn.cursor()

yb.execute(sql)

conn.commit()

yb.close()
conn.close()