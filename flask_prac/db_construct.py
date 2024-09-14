import sqlite3
import os

def cons_db(db_name):
    if not os.path.exists(db_name):
        con=sqlite3.connect(db_name)
        yb=con.cursor()

        dh_table='''create table navigation(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dh_name varchar ,
            dh_url varchar )'''

        art_table='''create table article(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title varchar ,
            img varchar,
            read integer ,
            content blob ,
            time datetime,
            navigation_id int)'''

        yb.execute(dh_table)
        yb.execute(art_table)
        con.commit()
        yb.close()
        con.close()
        # check
        print("数据库、表创建成功")
