# 创建库操作
# 引入我们的数据库操作模块
import sqlite3


# 初始化连接数据库
conn = sqlite3.connect("test.db")
# 把连接操作提交
conn.commit()
# 关闭防止浪费资源
conn.close()