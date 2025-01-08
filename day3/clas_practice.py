'''
创建一个员工工资管理系统，使用字典存储每个员工的名字和对应的工资。
分别输出所有员工姓名和工资。
添加新员工及其工资。
更新员工工资。
删除员工记录。
查找某个员工的工资。
'''

# staff_salary = dict(zip(["zhangsan","lisi","wangwu","zhaoliu"],[100,200,300,400]))

staff= {'zhangsan':1000}
staff2 = {"lisi":2000}
staff3 = {'wangsu': 3000}
staff.update(staff2)
staff.update(staff3)
print("每个员工的名字和对应的工资为：",staff)

# 分别输出所有员工姓名和工资
print("员工对应的工资为",staff.items())

# 添加新员工及工资
staff.setdefault("zhaoliu",90000)
print("现在公司内部的员工数量为：",staff)

# print(staff.items())



# 查找某员工工资
name = 'zhangsan'
print(f"员工{name}工资为：",staff[name])

# # 删除员工记录
staff.pop("zhaoliu")
print('目前公司内部员工：',staff)

print('------------------------------------分割线----------------------------------------')
"""
实战代码
创建一个学生成绩管理系统，使用字典存储每个学生的名字和对应的成绩。
分别输出所有学生姓名和成绩。
添加新学生及其成绩
更新学生成绩
删除学生记录
查找某个学生的成绩
"""
# 创建一个学生成绩管理系统，使用字典存储每个学生的名字和对应的成绩
student_score =  dict(zip(["zhangsan","lisi","wangwu","zhaoliu"],[90,80,300,70]))
print(student_score)


# 分别输出所有学生姓名和成绩
print('所有学生姓名和成绩为：',student_score.items())

# 添加新学生及其成绩
student_score.setdefault("xiaoxigua",60)
print("现在新学生及其成绩：",student_score)

# 更新学生成绩
if "xiaoxigua" not in student_score:
    student_score.setdefault("xiaoxigua",60)
else:
    print("当前学生已经存在系统中")

print("现在学生及其成绩：",student_score)


# 查找某个学生的成绩
student_score.keys('wangwu')

# 删除学生记录
student_score.popitem()
print("当前学生数量及成绩为：", student_score)