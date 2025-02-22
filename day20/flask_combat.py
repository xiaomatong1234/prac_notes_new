from flask import Flask,Blueprint,request

app = Flask(__name__)
register_users = {} # 用户注册信息 dic
blog_db = {1:{"title":"Pythonaa","author":"abc","content":"小细节都订单"},
           2:{"title":"java","author":"wee","content":"小细节都订单dv"},
           3:{"title":"php","author":"wewee","content":"小细节we都订单dv"}}# 博客信息 dic

# 1、定义蓝图对象
auth_blueprint = Blueprint('auth', __name__)
post_blueprint = Blueprint('post', __name__,url_prefix='/posts')

# 2、定义用户相关路由
@auth_blueprint.route('/register', methods=['POST'])
def user_register():
    # 获取json格式请求体
    register_json = request.json
    # 如果register_json为空，
    if not register_json or 'username' not in register_json or 'password' not in register_json:
        return {"errcode": -1,
                "msg": "Error data_json is none"},400
    # 获取请求体中对应的值,提取用户名和密码
    username = register_json.get('username')
    password = str(register_json.get('password'))
    # 用户名存在，提示用户名已存在
    if username in register_users:
        return {"errcode": -1,
                "msg": "username already exists"}
    # 校验密码长度是否大于6位，否，提示错误信息
    if len(password) < 6:
        return {"errcode": -1,
                "msg": "Error password length"}
    # 添加用户到字典
    register_users[username] = password
    print('注册成功！',register_users)
    return {"errcode": 0,
            "msg": "user auth successly",}
@auth_blueprint.route('/login', methods=['POST'])
def user_login():
    # 获取json请求体格式
    login_json = request.json
    # 校验请求数据中是否包含username/password,如果不包含，返回错误提示信息
    if not login_json or "username" not in login_json or "password" not in login_json:
        return {"errcode": -1,
                "msg": "Error user or password not exist"},400
    # 从请求中提取登陆的用户名、密码
    username = login_json.get('username')
    password = str(login_json.get('password'))
    print('登录成功：', {username: password})
    # 检查用户名是否存在，用户不存在返回错误响应
    if username not in register_users:
        return {"errcode": -1,
                "msg": "Error user not exist"}
    # 检查用户名和密码是否匹配，用户名和密码不匹配返回错误响应
    if register_users[username] != password:
        return {"errcode": -1,
                "msg": "Error username and password not matched"}
    # 登录成功
    return {"errcode": 0,
            "msg": "User login successfully"}
@post_blueprint.route('/create', methods=['POST'])
# 创建博客文章视图
def create_post():
    # 获取json格式请求体
    # 和前端约定请求体的格式{"post_title":"title","content":"content"}
    post_json = request.json
    if not post_json or 'title' not in post_json or 'author' not in post_json or 'content' not in post_json:
        return {"errcode": -1,
                "msg": "Error data_json is none"},400

    # 从请求中提取博客信息
    bolg_title = post_json.get('title')
    bolg_author = post_json.get('author')
    blog_content = post_json.get('content')

    # 获取所有博客标题列表
    post_title_list = [blog.get('title') for blog in blog_db.values()]
    # print(post_title_list)

    # 判断标题已经存在
    if bolg_title in post_title_list:
        return {"errcode": -1,
                "msg": "bolg title already exists"}

    # 生成新博客的id
    if len(blog_db.keys()) == 0:
        new_post_id = 1
    else:
        new_post_id = len(blog_db.keys()) + 1
    # 写入新博客数据
    blog_db[new_post_id] = {"title": bolg_title,
                            "author": bolg_author,
                            "content": blog_content}

    print('博客信息：',blog_db)
    return {"errcode": 0,
            "msg": "Post created successfully",
            "data":[
                {
                    'id': new_post_id,
                    'title': bolg_title,
                    'author': bolg_author,
                    'content': blog_content,
                }
            ]}
@post_blueprint.route('', methods=['GET'])
# 获得博客列表
def get_posts():
    if not blog_db:
        return {"errcode": -1,
                "msg": "Error data_json is none"}
    post_list = [{"id":post_id,"title":post['title'],'author':post['author'],'content':post['content']}
                 for post_id,post in blog_db.items()]
    return {"errcode": 0,
            "msg": "Post created successfully",
            "data": post_list}
@post_blueprint.route('/<int:bolg_id>', methods=['GET'])
# 根据博客ID获取博客详情
def get_post_details(bolg_id):
    if bolg_id in blog_db:
        return {"errcode": 0,
                "msg": "Post details successfully",
                "data": blog_db[bolg_id]
                }
@post_blueprint.route('delete/<int:bolg_id>', methods=['DELETE'])
# 检查博客是否存在
def delete_post(bolg_id):
    if not blog_db:
        return {"errcode": -1,
                "msg": "Error data_json is none"}
    if bolg_id not in blog_db:
        return {"errcode": -1,
                "msg": "bolg id not exists"}
    return {"errcode": 0,
            "msg": "Post deleted successfully",
            "data": blog_db.pop(bolg_id)}
if __name__ == '__main__':
    # 注册蓝图应用
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(post_blueprint)

    # 启动蓝图应用
    app.run(debug=True)