"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from flask import Flask, Blueprint, request, jsonify, render_template

app = Flask(__name__)

# 简单博客数据存储
# {"1": {"post_title": "title", "content": "content"}}
post_db = {"1": {"post_title": "java编程", "content": "java从入门到精通"}}

# 模拟的文章数据
posts = [
    {
        'id': 1,
        'title': 'Flask 入门',
        'author': 'Alice',
        'content': 'Flask 是一个轻量级的 Python Web 框架...'
    },
    {
        'id': 2,
        'title': 'Flask 模板技术',
        'author': 'Bob',
        'content': 'Flask 使用 Jinja2 模板引擎来渲染 HTML...'
    }
]

# 创建蓝图
post_blueprint = Blueprint("post", __name__, url_prefix="/posts")


# 创建博客
@post_blueprint.route("/create", methods=["POST"])
def create_post():
    # 获取 json 格式的请求体
    data = request.json
    # 和前端约定 {"post_title": "title", "content": "content"}
    if not data or "post_title" not in data or "content" not in data:
        return {
            "errcode": -1,
            "errmsg": "错误的博客数据"
        }
    # 从请求体中取出需要的数据
    post_title = data.get("post_title")
    content = data.get("content")
    # 判断标题已经存在的时候返回错误提示信息
    # {"1": {"post_title": "title", "content": "content"}}
    # 获取所有博客标题的列表
    post_title_list = [post.get("post_title") for post in post_db.values()]
    if post_title in post_title_list:
        return {
            "errcode": -1,
            "errmsg": "博客标题重复"
        }
    # 生成新博客的 id
    if len(post_db.keys()) == 0:
        new_post_id = 1
    else:
        new_post_id = len(post_db.keys()) + 1
    # 写入新博客数据
    post_db[str(new_post_id)] = {
        "post_title": post_title,
        "content": content
    }
    return {
        "errcode": 0,
        "errmsg": "博客添加成功",
        "datas": {
            "post_id": str(new_post_id),
            "post_title": post_title,
            "content": content
        }
    }

# 获取博客列表
@post_blueprint.route("")
def get_posts():
    return render_template("blog.html", posts=posts)

@post_blueprint.route("/<int:bid>")
def get_post_by_id(bid):
    # 需要展示的博客为
    result = None
    for post in posts:
        if post.get("id") == bid:
            result = post
    if result:
        return render_template("blog_info.html", post=result)
    else:
        return {
            "errcode": -1,
            "errmsg": "Post not found"
        }



if __name__ == '__main__':
    app.register_blueprint(post_blueprint)
    app.run(debug=True)
