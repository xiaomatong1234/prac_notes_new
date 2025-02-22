from flask import Flask,render_template

# 创建flask应用程序实例
app = Flask(__name__)
@app.route('/html')
def get_html(): # 设置路由和试图函数
    # 调用render_template方法，传入html文件的文件名称
    # html文件的文件名称必须在template目录下
    return render_template("home_page.html")

if __name__ == '__main__':
    app.run(debug=True)