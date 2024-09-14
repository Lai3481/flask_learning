import sqlite3 


conn = sqlite3.connect("test.db")





# create table 表名(字段名1 数据类型, 字段名2 数据类型, ... 字段名n 数据类型);
sql = """create table teacher_s(
            id integer PRIMARY KEY AUTOINCREMENT,
            name varchar,
            age integer,
            csrq datetime,
            derc text)"""

# 游标 你要执行数据库的时候，你需要一个执行的人
yb = conn.cursor()
# 执行sql语句
yb.execute(sql)
# 提交数据内容
conn.commit()
# 关闭资源
yb.close()
conn.close()
