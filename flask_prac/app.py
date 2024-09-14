from flask import Flask
from flask import request
from flask import render_template
from flask_cors import CORS

from db_construct import cons_db
from datetime import datetime
import random
import sqlite3
import os
import json

app = Flask(__name__)
CORS(app,resources=r"/*")

cons_db("ws_database.db")

# connect db
def db_connection(sql):
    con=sqlite3.connect("ws_database.db")
    yb=con.cursor()
    try:
        yb.execute(sql)
        if "select" in sql:
             res_data = yb.fetchall()
             yb.close()
             con.close()
             return res_data

        con.commit()
    except:
        print('sql formatting error')
  
    yb.close()
    con.close()

#construct dir
def dir_abs(img,pic_type):
    file_name= datetime.now().strftime("%Y%m%d%H%M%S")+"_"+ str(random.randint(1,5000))+"."+img.filename.rsplit('.')[1]
    basedir=os.path.abspath(os.path.dirname(__file__))
    basedir=basedir.replace("\\",'/')[2:] + f"/static/article_images/{pic_type}/"
    if not os.path.exists(basedir):
        os.makedirs(basedir)

    file_path=basedir+file_name
    img.save(file_path)
    print("文件路径是：",file_path)

    return file_name

# login api
@app.route('/login',methods=['POST'])
def login():
    u_name = request.form.get('username')
    p_word = request.form.get('password')
    if u_name == 'admin' and p_word == "123456":
        return {"status": "200", "msg": "登录成功"}
    else:
        return {"status": "400", "msg": "登录失败"}


# dh_list api
@app.route("/dh_list",methods=['GET'])
def dh_list():
    res=db_connection("""select * from navigation""")
    res_list = []
    for i in res:
        res_dict = {}
        res_dict["dh_id"] = i[0]
        res_dict["dh_name"] = i[1]
        res_dict["dh_url"] = i[2]
        res_list.append(res_dict)
    return res_list

# add_dh api
@app.route('/add_dh',methods=['POST'])
def add_dh():
    name = request.form.get("dh_name")
    url = request.form.get("dh_url")
    db_connection(f"""insert into navigation(dh_name,dh_url) values('{name}','{url}')""")
    return 'ok'

# delete api
@app.route('/delete_dh',methods=['DELETE'])
def delete_dh():
    id =request.args.get("dh_id")
    db_connection(f"""Delete from navigation where id = '{id}'""")
    return 'ok'

# update
@app.route('/update_dh',methods=['POST'])
def dh_update():
    id=request.form.get("dh_id")
    name=request.form.get("dh_name")
    url=request.form.get("dh_url")
    db_connection(f"""update navigation set dh_name='{name}',dh_url='{url}' where id='{id}'""")
    return 'ok'

# text content
@app.route('/save_head_picture',methods=['POST'])
def save_head_pic():
    img=request.files.get('head_img')
    img_file_name=dir_abs(img,"head_pic")
    url_host = "http://127.0.0.1:5000/static/article_images/head_pic/" + img_file_name
    res = {
            "errno":0,
            "data":{"url":url_host}
    }

    return json.dumps(res)

@app.route("/save_content_picture",methods=["POST"])
def save_content_pic():
    img=request.files.get("content_img")
    img_file_name=dir_abs(img,"content_pic")
    url_host = "http://127.0.0.1:5000/static/article_images/content_pic/" + img_file_name
    res = {
            "errno":0,
            "data":{"url":url_host}
    }

    return json.dumps(res)

@app.route('/article_insert',methods=["POST"])
def article_insert():
    img = request.form.get("fm_img")
    title = request.form.get("title")
    content = request.form.get("content")
    id = request.form.get("dh_id")

    article_time = str(datetime.now())[:10]

    db_connection(f"""insert into article (title,img,content,time,navigation_id) values('{title}','{img}','{content}','{article_time}','{id}')""")

    return 'ok'

@app.route('/article_list',methods=['GET'])
def article_list():
    res_article=db_connection("""select * from article""")
    res_list = []

    for i in res_article:
        print(i)
        res_dict= {}
        res_dict["id"] = i[0]
        res_dict["title"] = i[1]
        res_dict["img"] = i[2]
        res_dict["content"] = i[3]
        res_dict["f_t"] = i[5]
        res_dict["navigation_id"] = i[6]
        res_dict["preview"]  =  i[4][:5]
        res_list.append(res_dict)

    return res_list



# @app.route('/image/tiger')
# def tiger():
#     return render_template('/test.html')


# @app.route('/image/tiger2')
# def renjian():
#     return render_template('/test2.html')


if __name__ == '__main__':
    app.run(debug=True)
