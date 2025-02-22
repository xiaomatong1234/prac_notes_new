import json
from flask import Flask, Blueprint, render_template, request, redirect, url_for
import os

def create_app():
    app = Flask(__name__)

    # 应用启动时加载 JSON 数据
    with open('data/notes_db.json', 'r') as json_file:
        notes_db = json.load(json_file)

    notes_bp = Blueprint('notes', __name__, url_prefix='/notes')

    # 首页
    @app.route('/')
    def home_page():
        return render_template("home_page.html")

    # 笔记列表页
    @notes_bp.route('', methods=['GET'])
    def index():
        return render_template("index.html", notes=notes_db)

    # 添加笔记页面
    @notes_bp.route('/create', methods=['GET', 'POST'])
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
                note_id = len(notes_db) + 1

            # 新笔记内容
            new_note = {
                "id": note_id,
                "title": title,
                "author": author,
                "content": content
            }
            # 判断标题是否唯一
            if title not in [note['title'] for note in notes_db]:
                notes_db.append(new_note)
                # 更新 notes.json 文件
                with open('data/notes_db.json', 'w', encoding='utf-8') as file:
                    json.dump(notes_db, file, ensure_ascii=False, indent=4)
            else:
                return {
                    'errcode': -1,
                    'errmsg': 'Note titles are repeated'
                }

            return redirect(url_for("notes.note_detail", nid=note_id))  # 页面重定向，跳转到新笔记详情页

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
                "errcode": -1,
                "errmsg": "note not found"
            }, 400

    # 注册蓝图
    app.register_blueprint(notes_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=10000)
