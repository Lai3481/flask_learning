import sqlite3

conn = sqlite3.connect("test.db")

# alter table 表名 add 新增的字段名 数据类型;

sql = """alter table teacher add idcard char"""

yb = conn.cursor()

yb.execute(sql)

conn.commit()

yb.close()
conn.close()