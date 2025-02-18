from flask import Flask, request, jsonify

app = Flask(__name__) # 创建flask实例
# 用于存储已注册用户的字典
register_users = {}

@app.route('/register',methods=['POST'])
# 定义注册路由
def register():
    # 获取json格式请求体
    data_json = request.json

    if data_json is None:
        return {"errcode": -1,
                "msg": "Error data_json is none"}
    # 校验数据中是否存在username和password,如果不包含则返回错误提示信息
    if "password" not in data_json or "username" not in data_json:
        return {"errcode": -1,
                "msg": "Error user or password not exist"}
    # 获取请求体中对应的值,提取用户名和密码
    username = data_json.get('username')
    password = str(data_json.get('password'))

    # 检查用户名是否已经存在，用户已存在则返回错误响应信息
    if username in register_users:
        return {"errcode":-1,
            "msg":"Error username exist"}
    # 检查密码是否符合要求（简单的长度检查），密码小于6位返回错误信息
    if len(password) < 6:
        return {"errcode": -1,
            "msg": "Error password length"}
    # 符合规则的用户添加到字典中保存
    register_users[username] = password
    print('注册成功！',{username: password})
    # 注册成功
    return {"errcode": 0,
            "msg": "User registered successfully"}



@app.route('/login',methods=['POST'])
def login():
    # 获取json请求体格式
    login_json = request.json
    # 校验请求数据中是否包含username/password,如果不包含，返回错误提示信息
    if "username" not in login_json or "password" not in login_json:
        return {"errcode": -1,
                "msg": "Error user or password not exist"}
    # 从请求中提取登陆的用户名、密码
    username = login_json.get('username')
    password = str(login_json.get('password'))
    print('登录成功：',{username: password})
    # 检查用户名是否存在，用户不存在返回错误响应
    if username not in register_users:
        return {"errcode": -1,
                "msg": "Error user not exist"}
    # 检查用户名和密码是否匹配，用户名和密码不匹配返回错误响应
    if password != register_users.get(username):
        return {"errcode": -1,
                "msg": "Error username and password not matched"}
    # 登录成功
    return {"errcode": 0,
            "msg": "User login successfully"}

if __name__ == '__main__':
    app.run(debug=True)