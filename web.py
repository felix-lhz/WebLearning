from flask import Flask,render_template,request
import pymysql

app = Flask(__name__) # create an instance of the Flask class

@app.route('/') # route() decorator to tell Flask what URL should trigger our function
def index():
    # render_template() function to render the HTML file we’ve just created
    return render_template('index.html')

@app.route('/register',methods = ['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        user = request.form.get("username")
        pwd = request.form.get("passward")
        gender = request.form.get("gender")
        city = request.form.get("city")
        print(user, pwd, gender, city)
        # 将用户信息写入文件中实现注册、写入到excel中实现注册、写入数据库中实现注册

        # 2.给用户再返回结果
        return 'Done'

@app.route('/xiaomi')
def xiaomi():
    return render_template('xiaomi.html')

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/background')
def background():
    return render_template('background.html')

@app.route('/javascripts')
def runningHorseLamp():
    return render_template('javaScripts.html')

@app.route('/addData')
def addData():
    return render_template('addData.html')

@app.route('/add/user',methods = ['GET','POST'])
def addUser():
    if request.method == 'GET':
        return render_template('addUser.html')
    elif request.method == 'POST':
        username  = request.form.get('username')
        passward = request.form.get('password')
        mobile = request.form.get('mobile')
        
        #1.连接数据库
        conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd="felix152!", charset='utf8', db='NIS3368')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        
        # 2.发送指令（ *** 千万不要用字符串格式化去做SQL的拼接，安全隐患SQL注入***）
        cursor.execute("insert into admin(username,password,mobile) values('wupeiqi','qwe123','15155555555')")
        conn.commit()
        cursor.execute("select * from admin where id > %s", [2, ])
        
        # 获取符合条件的所有数据，得到的是 [ 字典,字典, ]    空列表
        data_list = cursor.fetchall()
        for row_dict in data_list:
            print(row_dict)
        
        # 3.关闭
        cursor.close()
        conn.close()
        
        return "success"
    
if __name__ == '__main__':
    app.run() # start the development server with the run