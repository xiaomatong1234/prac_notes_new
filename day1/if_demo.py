# # school = input('请输入你的学校：')
# # if school  == 'hogwarts':
# #     print('欢迎欢迎👏👏👏👏👏👏👏👏👏----魔法师🧙魔法师🧙')
# # elif school == '森与海':
# #     print('❌❌❌❌❌❌你是个麻瓜麻瓜麻瓜----🪄🪄测试开发')
# # elif school == '你个小可爱':
# #     print('土豆！！！你是个老登。。。')
# # else:
# #     print('打铁花！霍！！！！霍霍！！霍霍霍！！')
#
#
# # 接受用户输入姓名
# name = input("请输入你的名字：\n")
#
# # 接受用户输入喜欢的科目，用数字代表
# hobby = int(input("请选择你擅长/喜欢的科目，文科选1，理科选2：\n"))
#
# # 判断如果喜欢的科目是文科
# if hobby == 1:
#     # 接受用户输入想要的职业，用户数字表示
#     orientation_choose = int(input("请选择你想要的职业，历史选1，地理选2：\n"))
#     # 判断如果选择是1，想要的职业是历史
#     if orientation_choose == 1:
#         orientation = "历史"
#     # 不是1，想要的职业是地理
#     else:
#         orientation = "地理"
# # 喜欢的不是文科
# else:
#     orientation_choose = int(input("请选择你想从业的方向：数学选1，生物选2，编程选3\n"))
#     # 接受用户输入一个理科的方向，用数字表示
#     if orientation_choose == 1:
#         orientation = "数学"
#     elif orientation_choose == 2:
#         orientation = "生物"
#     # 方向不想要数学和生物，剩下编程
#     else:
#         # 接受用户输入，选择编程的就业方向，用数字表示
#         coder_choose = int(input("请选择你想从事的软件职业方向：测试选1，开发选2，产品选3，项目经理选4\n"))
#         if coder_choose == 1:
#             orientation = "测试"
#         elif coder_choose == 2:
#             orientation = "开发"
#         elif coder_choose == 3:
#             orientation = "产品"
#         else:
#             orientation = "项目经理"
# print(f"{name} 同学，你意向的职业为: {orientation}")
'''
编写一个 Python 程序，模拟乘坐公交车过程，并且可以有座位坐下。要求：输入公交卡当前的余额，只要不低于2元，就可以上公交车；如果车上有空座位，就可以坐下
'''
#
# money = float(input('请输入公交卡当前的余额: \n'))
#
# if money >= 2:
#     print('可以上公交车')
#     bus_sit = int(input('请选择公交车上是否有座位：有座位选择1，没有座位选择2 \n'))
#     if bus_sit == 1:
#         print('公交车上有座位，可以座')
#     else:
#         print('公交车上没座位，站着！')
# else:
#     print('公交卡余额不足，不允许上公交车')

# # 判断用户输入的余额
# money = float(input('请输入公交卡当前的余额: \n'))
# if money >= 2:
#     print('可以上公交车')
#     bus_sit = int(input('请选择公交车上是否有座位：有座位选择1，没有座位输入其它数字 \n'))
#     if bus_sit == 1:
#         print('公交车上有座位，可以坐')
#     else:
#         print('公交车上没座位，站着！')
# else:
#     print('公交卡余额不足，不允许上公交车')
# '''
# 实战：简单计算器
# 需求：编写一个简单的 Python 程序，支持加减乘除四种运算。
# 需求分析：用户输入两个数字和一个运算符，程序计算并输出结果。
#
# 输入第一个数字：5
# 输入第二个数字：3
# 输入运算符：+
# 输出结果：8
# '''
# num1 = float(input('请输入第1个数字：'))
# signal = str(input('请输入加减乘除四种运算符号:'))
# num2 = float(input('请输入第2个数字：'))
# result = None
# if signal == '+':
#     result = num1 + num2
# elif signal == '-':
#     result = num1-num2
# elif signal == '*':
#     result = num1*num2
# elif signal == '/':
#     if num2 != 0:
#         result = num1/num2
#     else:
#         print('当前除数不能为0')
# elif signal == '%':
#     result = num1%num2
# elif signal == '**':
#     result = num1**num2
# elif signal == '//':
#     result = num1//num2
# else:
#     result = '运算符输入错误'
#     print('输入不符合要求，请重新输入。。。。')
# print('运算结果为:', result)
