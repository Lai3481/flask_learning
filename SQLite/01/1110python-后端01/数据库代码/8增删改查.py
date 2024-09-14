import sqlite3 


conn = sqlite3.connect("test.db")


#语法
# insert into 表名 values(值1，值2，值3...),(值1，值2，值3...);


# 插入数据
# create table 表名(字段名1 数据类型, 字段名2 数据类型, ... 字段名n 数据类型);
# sql = """insert into teacher_s values(2,"1文景",28,"2022-11-11 22:22:22","测试")
# """

# 删除数据
# 语法
# delete from 表名 where 条件;
# 注意: delete语句后如果不加where条件,所有记录会全部清空； 例 delete from 表名

# sql  = """delete from teacher_s where name='1文景' """


# 修改数据
# 语法
# update 表名 set 字段1=新的值,字段2=值... where 条件;

# 注意: update语句后如果不加where条件,这一列下所有满足条件的都会被改变； 例 update 表名 set 字段=值
age = 18
sql =f"""update teacher_s set age={age} where name='文景' """


# 游标 你要执行数据库的时候，你需要一个执行的人
yb = conn.cursor()
# 执行sql语句
yb.execute(sql)
# 提交数据内容
conn.commit()
# 关闭资源
yb.close()
conn.close()
