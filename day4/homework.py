"""
课后作业
创建一个学生成绩管理系统，学生的信息包括 姓名（字符串）、课程名称和成绩。使用函数封装每个功能。主菜单展示系统功能。

- 添加学生成绩（学生姓名、课程名称、成绩）。
- 查询某个学生的成绩。
- 更新学生的成绩。
- 删除学生的成绩记录。
- 显示所有学生的成绩。

"""
# 创建一个学生成绩管理系统，学生的信息包括 姓名（字符串）、课程名称和成绩

def students_management(**kwargs):
    # 根据姓名查询学生成绩
    if kwargs['name'] == 'tom':
        print(f'{kwargs["name"]}同学的成绩为：', kwargs['score'])

    # 更新学生成绩
    if  kwargs['name']=='tom' :
        kwargs['score'] = 20
        print('更新学生tom的成绩：',kwargs)


    # 删除学生成绩
    if kwargs['name'] == 'Ana':
        del kwargs['name']
        print('Ana同学的成绩已被删除')

    # 显示所有学生成绩

    return  kwargs


if __name__ == '__main__':
    # 添加学生成绩
    print('显示所有学生的成绩：',
        students_management(name='tom', class_name="python课程", score=100),
          students_management(name='Tim', class_name="Jav课程", score=90),
          students_management(name='Ana', class_name="Java课程", score=80),
          students_management(name='Tim', class_name="Php课程", score=70),
          students_management(name='yy', class_name="go课程", score=60),
          students_management(name='KK', class_name="ruby课程", score=50))



# # 查询学生成绩
# def student_management_search(**kwargs):
#     # 根据姓名查询学生成绩
#     if kwargs['name'] == 'tom':
#         return '学生成绩为：', kwargs['score']
# if __name__ == '__main__':
#     print(student_management_search())

