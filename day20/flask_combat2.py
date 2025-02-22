"""实战：用户认证系统中的路由跳转"""
from flask import Flask,request,redirect,url_for
app=Flask(__name__)
users_db = {
    'feier': {
        'password': 'adminpass',
        'role': 'admin',
        # 状态包含已登陆 logged，未登录 unlogged
        'status': 'unlogged'
    },
    'lily': {
        'password': 'userpass',
        'role': 'user',
        'status': 'unlogged'
    }
}
@app.route('/login',methods=['GET','POST'])
def login():
    """
    跳转登录
    :return:
    """
    # get请求：显示登录页面
    if request.method == 'GET':
        return "登录页面"
    # post请求：验证用户信息
    if request.method == 'POST':
        """
        1、校验请求数据是否包含用户名、密码
        2、检查用户名是否存在
        3、校验密码是否正确
        4、用户状态标记为logged. ????
        5、重定向/dashboard路由
        """
        user_json = request.get_json()
        # 1、校验请求数据是否包含用户名、密码
        if not user_json or 'username' not in user_json or 'password' not in user_json:
            return {
                'errcode':-1,
                'errmsg':'请求信息不存在'
            },400

        # 从json请求中获取用户信息
        username = user_json.get('username')
        password = str(user_json.get('password'))

        # 2、检查用户名是否存在
        if username not in users_db:
            return {
                'errcode': -1,
                'errmsg': '用户名不存在'
            }
        # 3、校验密码是否正确
        if users_db[username]['password'] != password:
            return {
                'errcode': -1,
                'errmsg': '密码错误'
            }

        # 4、标记用户名为已登录
        users_db[username]['status'] = 'logged'
        # 5、重定向/dashboard路由
        return redirect(url_for('dashboard_page',username=username))


@app.route('/dashboard/<string:username>',methods=['GET','POST'])
def dashboard_page(username):
    """
    1、检查用户状态是否为logged,未登录，跳转到/login路由
    2、用户角色判断：
        admin：显示管理页面
        user：重定向/profile
    :return:
    """
    # 检查用户状态是否为logged,未登录，跳转到/login路由
    if users_db[username]['status'] != 'logged':
        return redirect(url_for('login_page'))
    # admin：显示管理页面
    if users_db[username]['role'] == 'admin':
        return "Welcome to the Admin Dashboard"
    # user：重定向/profile
    elif users_db[username]['role'] == 'user':
        return redirect(url_for('profile_page',username=username))


@app.route('/profile/<string:username>',methods=['GET','POST'])
def profile_page(username):
    """
    1、检查用户状态是否为logged,未登录，跳转至/login路由
    2、显示用户的个人资料页面
    :return:
    """
    # 1、检查用户状态是否为logged,未登录，跳转至/login路由
    if users_db[username]['status'] != 'logged':
        return redirect(url_for('login_page'))
    # 显示用户的个人资料页面
    return f"Welcome to {username}'s Profile!"

if __name__ == '__main__':
    app.run(debug=True)
