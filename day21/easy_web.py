from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("easy.html")
@app.route('/login',methods=['POST'])
def login():
    return 'welcome to login'

if __name__ == '__main__':
    app.run(debug=True)