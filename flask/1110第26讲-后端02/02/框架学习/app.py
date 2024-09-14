# 引入框架
from flask import Flask
from flask import request

# 实例化一个flask对象
app = Flask(__name__)


@app.route("/index")
def func1():
    return "你好我是文景12134123123"


# 函数名称不能重复,路由地址也不能重复
@app.route("/index1")
def func2():
    # "怎么写函数，怎么写内容"
    return "dsadsa"

# 可以多级目录
@app.route("/login/index1")
def login():
    return "欢迎登录1"


# 写一个get请求
@app.route("/book/zoo/1",methods=["GET"])
def mpp1():
    return "拿到书籍是动物园的第一页"


# 写一个get请求
@app.route("/book/zoo/2",methods=["GET"])
def mpp2():
    return "拿到书籍是动物园的第二页"



# 写一个get请求
@app.route("/mpp",methods=["GET"])
def mpp():
    return "我是get请求"


# 写一个get请求
@app.route("/post_pp",methods=["POST"])
def post_pp():
    return "我是post请求"



# 写一个登录接口
@app.route("/login/web",methods=["POST"])
def login_web():
    # 用户名
    username = request.form.get("username")
    # 密码
    password = request.form.get("password")
    print("输入的用户名是：",username)    
    print("输入的密码是：",password)
    # return "测试"
    if username == "admin" and password =="123456":
        return "欢迎登录"
    else:
        return "用户名和密码不匹配"




if __name__ =="__main__":
    # 启动我们的web服务
    app.run(port=8000,debug=True)