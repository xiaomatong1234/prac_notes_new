import json

from flask import Flask,Blueprint, render_template, request, redirect, url_for
import os

# 打印当前工作目录
print ("Current working directory:", os.getcwd ())
print("Template folder:", os.path.join(os.getcwd(), 'templates'))

app = Flask(__name__,template_folder='templates')
# 应用启动时加载 JSON 数据
with open('data/notes_db.json','r') as json_file:
    notes_db = json.load(json_file)

notes_bp = Blueprint('notes', __name__, url_prefix='/notes')
"""
首页展示笔记：

首页 (index.html) 显示所有笔记的基本信息：书名、作者、笔记创建时间。
你可以使用一个路由（例如 /）来显示笔记列表，通过 render_template 渲染 HTML 页面。
在 index.html 中使用循环结构展示每篇笔记的摘要，并为每篇笔记设置一个链接，点击后进入笔记详情页面。

笔记详情页面：
每个笔记详情页面 (note_detail.html) 显示笔记的全部内容。
你可以在路由中使用 URL 参数来获取笔记的 ID 或者其他标识符，然后渲染该笔记的完整内容。
"""

# 首页
@app.route('/')
def home_page():
    return render_template("home_page.html")
# 笔记列表页
@notes_bp.route('', methods=['GET'])
def index():
    return render_template("index.html", notes=notes_db)

# 添加笔记页面
@notes_bp.route('/create',methods=['GET','POST'])
def create_note():
    if request.method == 'GET':
        return render_template("create_note.html")  # 展示填写新笔记的表单页面
    if request.method == 'POST':
        # 获取表单数据
        data = request.form
        title = data.get('title')
        author = data.get('author')
        content = data.get('content')

        # 生成笔记id
        if len(notes_db) == 0:
            note_id = 1
        else:
            note_id =  len(notes_db) + 1

        # 新笔记内容
        new_note =  {
            "id": note_id,
            "title": title,
            "author": author,
            "content": content
        }
        # 判断标题是否唯一
        if title not in [note['title'] for note in notes_db]:
            notes_db.append(new_note)
            # 更新 notes.json 文件
            with open('data/notes_db.json','w', encoding='utf-8' ) as file:
                json.dump(notes_db,file,ensure_ascii=False, indent=4)
        else:
            return {
                'errcode':-1,
                'errmsg':'Note titles are repeated'
            }

        return redirect(url_for("notes.note_detail",nid=note_id)) # 页面重定向，跳转到新笔记详情页
# 笔记详情页
@notes_bp.route('/<int:nid>', methods=['GET'])
def note_detail(nid):
    note_content = None
    for note in notes_db:
        if note.get("id") == nid:
            note_content = note
    if note_content:
        return render_template("note_detail.html", note=note_content)
    else:
        return {
            "errcode":-1,
            "errmsg":"note not found"
        },400
app.register_blueprint(notes_bp)
if __name__ == '__main__':


    app.run(debug=True)


