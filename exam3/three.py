"""
编写一个 Python 程序，接收一个包含学生姓名和成绩的字典，输出成绩最高的学生姓名。
"""
def stu():
    lst = []
    for stu_name,stu_grade in stu_dic.items():
        lst.append((stu_name, stu_grade))
    # print(sorted(lst)[0])
    name,grade = sorted(lst)[0]
    print('成绩最高的学生姓名为：',name)

stu_dic = {
    "zhangsan":12,
    "lisi":17,
    "wangwu":16,
}
stu()