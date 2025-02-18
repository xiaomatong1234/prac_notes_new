from flask import Flask
# 创建Flask应用程序实例  __name__：当前函数的名称
app = Flask(__name__)

# 定义路由和视图函数
@app.route('/') # 基本路由
def hello(): # 视图函数
    return 'Hello 1234'
@app.route('/about') # 基本路由
def about():
    return 'About HomePage'

@app.route('/about/<username>') # 动态路由
def user_info(username):
    return f'Welcome {username} login'
@app.route('/post/<username>/<int:usr_id>') #限定路由
def user_infos(username,usr_id):
    return f'Welcome {username} {usr_id}'
@app.route('/user',methods=['GET'])  # get请求
def get_method():
    return f'Method is GET'
@app.route('/post',methods=['POST']) # post请求
def post_method():
    return f'Method is POST'
@app.route('/user/put',methods=['PUT'])  # put 请求
def put_method():
    return f'Method is PUT'
@app.route('/user/delete',methods=['DELETE'])  # delete请求
def delete_method():
    return f'Method is DELETE'

if __name__ == '__main__':
    # 访问应用程序
    app.run()
