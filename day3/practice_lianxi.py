
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

employees["ddd"]= {}
employees['ddd']["attendance"]= [20, 211, 19]
employees['ddd']['extra_info'] = {"position": "Manager","contact": "11112345678" }
print(employees)

