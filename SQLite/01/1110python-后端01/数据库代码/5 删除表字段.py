import sqlite3

conn = sqlite3.connect("test.db")

# 删除字段语法(drop)
#     alter table 表名 drop 要删除的字段名; 
sql = "alter table teacher drop derc;"

yb = conn.cursor()

yb.execute(sql)

conn.commit()

yb.close()
conn.close()