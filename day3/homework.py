"""
课后作业
- 创建一个包含员工信息的管理系统，员工的信息包括 姓名（字符串）、月考勤天数（列表，每月天数） 和 额外信息（字典，存储例如职位和联系方式）。
- 添加新员工：向系统中添加一个新员工的所有信息（包括姓名、考勤天数和额外信息）。
- 更新员工考勤：修改指定员工某个月的考勤天数。
- 删除员工信息：从系统中删除某个员工的信息。
- 获取员工列表：输出所有员工的姓名。
- 查找员工信息：通过姓名查找并输出该员工的完整信息。
"""

employees = {
    "John": {
        # 一个季度的考勤天数
        "attendance": [20, 22, 19],
        # 附加信息
        "extra_info": {
            # 职位
            "position": "Manager",
            # 联系方式
            "contact": "13012345678"
        }
    }
}
employees["ddd"]["extra_info"]["position"] = "Manager"

# 添加新员工：向系统中添加一个新员工的所有信息（包括姓名、考勤天数和额外信息）
print('----添加新员工：向系统中添加一个新员工的所有信息（包括姓名、考勤天数和额外信息）----')
new_employee = {"lucid":{
"attendance":[112,12,34],
"extra_info": {
            # 职位
            "position": "staff",
            # 联系方式
            "contact": "13051786350"
        }

}}

employees.update(new_employee)
print(f'添加新员工后系统中员工信息为：{employees}',end='\n\n')


# 更新员工考勤：修改指定员工某个月的考勤天数
print("----更新员工考勤：修改指定员工某个月的考勤天数----")
employees["lucid"]["attendance"]= "[20, 12, 19]"
print(f'更新员工lucid考勤：{employees}',end='\n\n')

# 获取员工列表：输出所有员工的姓名。
print('----获取员工列表：输出所有员工的姓名----')
print('输出所有员工的姓名:',employees.keys())


# 查找员工信息：通过姓名查找并输出该员工的完整信息。
print('----查找员工信息：通过姓名查找并输出该员工的完整信息----')
print('通过姓名查找John并输出John的完整信息',employees.get("John"),end='\n\n')



#  删除员工信息：从系统中删除某个员工的信息。
print('----删除员工信息：从系统中删除某个员工的信息----')
print('从系统中删除员工lucid的信息',employees.pop('lucid'),end='\n\n')

