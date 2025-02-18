from flask import Flask

app = Flask(__name__)

@app.route("/tasks",methods=['GET']) # 获取任务列表
def get_tasks():
    return 'GET请求获取任务列表'

@app.route("/tasks",methods=['POST']) # 创建任务
def create_task():
    return 'POST请求创建新任务'

@app.route("/tasks/<int:task_id>",methods=['PUT']) # 更新任务状态
def update_task(task_id):
    return f'PUT请求更新任务id为{task_id}的任务'

@app.route("/tasks/<int:task_id>",methods=['DELETE']) # 删除任务
def delete_task(task_id):
    return f'DELETE请求删除任务id为{task_id}的任务'


if __name__ == '__main__':
    app.run()