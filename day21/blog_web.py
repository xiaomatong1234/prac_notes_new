from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
blogs_db = [
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
# 渲染所有博客文章标题
@app.route('/blog')
def show_all_blogs():
    return render_template('blog_web.html', blogs=blogs_db)

# 渲染单篇文章详情
@app.route('/blog/<int:blog_id>')
def show_blog_info(blog_id):
    # 需要展示的博客信息
    blog_content = None
    for blog in blogs_db:
        if blog.get('id') == blog_id:
            blog_content = blog
    if blog_content:
        return render_template('blog_web_info.html',content=blog_content)
    else:
        return {
            "errcode": -1,
            "errmsg": "Blog not found"
        }


if __name__ == '__main__':
    app.run(debug=True)
