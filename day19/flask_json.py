
from flask import Flask,request

app = Flask(__name__)

@app.route('/data',methods=['POST'])
def get_post():
    # 获取json格式请求体
    data_json = request.json
    print(data_json)
# 获取请求体中对应字段的值
    name = data_json.get('name')
    age = data_json.get('age')
    return {"Name": name, "Age": age}

if __name__ == '__main__':
    app.run(debug=True)
