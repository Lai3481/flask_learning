# 引入框架
from flask import Flask
from flask import request
from flask import render_template

# 实例化一个flask对象
app = Flask(__name__)


@app.route("/index")
def func1():
    # # 查询所有的书籍
    # data = ["三国演义",]
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

# "get请求的登录" 是不允许的，因为非常的不安全
@app.route("/get_login",methods=["GET","POST"])
def get_login():
    # 获取用户名 args 这个函数只能获取get请求里的参数
    username = request.args.get("username")
    # 获取密码
    password = request.args.get("password")
    print("args输入的用户名是：",username)    
    print("args输入的密码是：",password)
    # 用户名 form post请求里的参数
    username = request.form.get("username")
    # 密码
    password = request.form.get("password")
    print("form提交的输入的用户名是：",username)    
    print("form提交的输入的密码是：",password)

    return "我是get请求的登录"


# 写一个get请求
@app.route("/login/1",methods=["GET"])
def login1():
    return render_template("login.html")


# 写一个get请求
@app.route("/index/1",methods=["GET"])
def index1():

    return render_template("index.html")



# 写一个get请求
@app.route("/index/2",methods=["GET"])
def index2():
    
    return render_template("index2.html")


# 写一个get请求
# 这是资源sunshangxiang 图片
@app.route("/get/sunshangxiang/img",methods=["POST"])
def index3():
    print("我是请求：",request.method)    
    xx = "病毒"
    file_name = request.files.get("file_name")
    print(file_name)
    return render_template("data/1110_index.html")
    # return "10011"
    # return ["xx","yy","xccc"]
    # return ["xx","yy","xccc"]







if __name__ =="__main__":
    # 启动我们的web服务
    app.run(port=8000,debug=True)