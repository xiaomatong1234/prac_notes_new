from flask import Flask,redirect,url_for
app =Flask(__name__)
users_list = ['xiaoming','lisi','zhangsan']

@app.route('/home/<user>',methods=['GET','POST'])
def home_page(user):
    # 访问学者在列表中，跳转至/dashboard
    if user in users_list:
        return redirect(url_for('dashboard_page',user_name=user))
    # 访问学者未满足条件，跳转至/login路由
    return redirect(url_for('login_page'))



@app.route('/dashboard',methods=['GET','POST'])
def dashboard_page():
    return 'Welcome to the Dashboard!'

@app.route('/login',methods=['GET','POST'])
def login_page():
    return 'Please log in'


if __name__ == '__main__':
    app.run(debug=True)