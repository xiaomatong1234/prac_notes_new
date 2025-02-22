# """
# 使用 Flask 创建一个应用，实现一个登录接口，接收用户名和密码，
# 如果用户名是 "admin" 且密码是 "1234"，返回欢迎信息，否则返回错误信息。
# """
# from flask import Flask,request
# app = Flask(__name__)
# users_db = {
#    "admin": 1234
# }
# @app.route('/login',methods=['POST'])
# def login():
#     data_json = request.json
#     if not data_json or 'username' not in data_json or 'password' not in data_json:
#         return {
#             "errcode":-1,
#             "errmsg": "not data_json"
#         },400
#     username = data_json.get('username')
#     password = data_json.get('password')
#
#     if not users_db:
#         return {
#             "errcode":-1,
#             "errmsg": "users_db not exist"
#         },400
#
#     if username not in users_db:
#         return {
#             "errcode": -1,
#             "errmsg": "username not exist"
#         }, 400
#
#     if users_db[username] != password:
#         return {
#             "errcode": -1,
#             "errmsg": "username or password is wrong"
#         }, 400
#
#     return {
#         "errcode":0,
#         "errmsg": "login success"
#     },200
#
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

users_db = {
    "admin": "1234"
}

@app.route('/login', methods=['POST'])
def login():
    data_json = request.json
    if not data_json or 'username' not in data_json or 'password' not in data_json:
        return jsonify({
            "errcode": -1,
            "errmsg": "not data_json"
        }), 400

    username = data_json.get('username')
    password = str(data_json.get('password'))

    if not users_db:
        return jsonify({
            "errcode": -1,
            "errmsg": "users_db not exist"
        }), 400

    if username not in users_db:
        return jsonify({
            "errcode": -1,
            "errmsg": "username not exist"
        }), 400

    if users_db[username] != password:
        return jsonify({
            "errcode": -1,
            "errmsg": "username or password is wrong"
        }), 400

    return jsonify({
        "errcode": 0,
        "errmsg": "login success"
    }), 200

if __name__ == '__main__':
    app.run(debug=True)