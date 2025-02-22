"""
实战：学生管理系统
定义学生类，包含 sid，name，age，gender 四个属性。需要定义一个把对象转为字典的方法 to_dict()


定义学生管理系统后端服务，使用蓝图管理路由：
添加新学生信息：输入学号、姓名、年龄和性别，添加到学生系统（字典）中，学号为 key，学生对象为 value。
通过学号查询学生信息：输入学号，查询并显示对应学生的信息。
通过学号修改学生信息：根据输入的学号修改对应学生的姓名、年龄和性别。
通过学号删除学生信息：输入学号，删除对应的学生信息。
"""
from flask import Flask,Blueprint,request

app =Flask(__name__)
# 1、定义蓝图对象
stu_manager_blueprint = Blueprint('stu_manager', __name__,url_prefix='/students')

students_db ={}  # 键：学生sid 值：学生对象 {sid:{sid,name,age,gender}}

# 创建新学生
@stu_manager_blueprint.route('',methods=['POST'])
def add_student():
    """
    1、请求数据：sid,name(必填) age,gender(选填)
    2、校验数据是否完整
    3、判断学生id是否存在
    4、添加学生到数据库/字典
    """
    # 获得json格式的请求体
    stu_json= request.json
    # 判断请求json是否存在
    if not stu_json or 'sid' not in stu_json or 'name' not in stu_json:
        return {
            'errcode':-1,
            'errmsg':"Error data_json is none"
        },400
    # 获取请求体中对应的值
    sid = stu_json.get('sid')
    name = stu_json.get('name')
    age = stu_json.get('age')
    gender = stu_json.get('gender')

    # 判断学生id是否存在
    if sid in students_db:
        return {
            'errcode': -1,
            'errmsg': "学生id已存在"}

    # 获取请求体中对应的值
    stu = Student(sid=sid, name=name, age=age, gender=gender)
    students_db[sid] = stu

    print('学生信息：',stu.to_dict())
    return {
        "errcode":0,
        "errmsg":"ok",
        "datas": [
            {"sid":sid,
             "name":name,
             "age":age, # 可能为None
             "gender":gender # 可能为None
             }
        ]
    }
@stu_manager_blueprint.route('/list',methods=['GET'])
def show_students():
    """获取所有学生信息"""
    if not students_db:
        return{
            'errcode':-1,
            'errmsg':"students_db is empty"
        }
    # 获取学生列表
    stu_lst = [{"sid":sid,"name":student.name,"age":student.age,"gender":student.gender} for sid,student in students_db.items()]
    # stu_lst = [student.to_dict() for sid,student in students_db.items()]

    print('展示所有学生信息：',stu_lst)
    # print("学生id：",type(stu_lst[0]['sid']))
    return {
        "errcode":0,
        "errmsg":"Show all students successfully",
        "datas":stu_lst
    },200

@stu_manager_blueprint.route('/<int:sid>',methods=['GET'])
def id_query_student(sid):
    """
    1、通过学号查询学生信息
    2、返回学生信息字典
    """
    # print(type(sid))
    if sid not in students_db:
        return {
            'errcode':-1,
            'errmsg':'Sid not exists'
        }
    student_info = students_db[sid]
    return {
        "errcode":0,
        "errmsg":"Query student info successfully",
        "datas":student_info.to_dict()
    },200

@stu_manager_blueprint.route('/<int:sid>',methods=['PUT'])
def id_modify_student(sid):
    """
    1、通过学号更新学生信息
    2、必填：name、age、gender
    """
    if sid not in students_db:
        return {
            'errcode': -1,
            'errmsg': 'Sid not exists'
        }
    new_info = request.json
    if not new_info or 'name' not in new_info or 'age' not in new_info or 'gender' not in new_info:
        return {
            'errcode': -1,
            'errmsg': 'Error data_json is none'
        },400

    # 从json中获取数据
    new_name = new_info.get('name')
    new_age = new_info.get('age')
    new_gender = new_info.get('gender')

    # 更新学生信息
    student = students_db[sid] # # 获取学生对象
    student.name = new_name
    student.age = new_age
    student.gender = new_gender
    print('更新后学生信息：',student.to_dict())
    return {
        "errcode":0,
        "errmsg":"Modify student info successfully",
        "datas":student.to_dict()
    },200

@stu_manager_blueprint.route('/<int:sid>',methods=['DELETE'])
def id_delete_student(sid):
    """通过学号删除学生信息"""
    if sid not in students_db:
        return {
            'errcode': -1,
            'errmsg': 'Sid not exists'
        }, 400
    student = students_db[sid] # 获取学生对象
    students_db.pop(sid)
    print('删除的学生信息：',student.to_dict())
    return{
        "errcode": 0,
        "errmsg": "Delete student successfully",
    },200
class Student:
    # 定义学生类，包含 sid，name，age，gender 四个属性
    def __init__(self, sid, name, age=None, gender=None):
        self.sid = sid
        self.name = name
        self.age = age
        self.gender = gender
    # 定义一个把对象转为字典的方法
    def to_dict(self):
        return {'sid': self.sid, 'name': self.name, 'age': self.age, 'gender': self.gender}

if __name__ == '__main__':
    # 3、注册蓝图应用
    app.register_blueprint(stu_manager_blueprint)
    # 4、启动蓝图应用
    app.run(debug=True)