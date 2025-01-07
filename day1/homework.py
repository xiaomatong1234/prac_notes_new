score = float(input('请输入一个分数：'))
degree = None
if score >= 90:
    degree = 'A'
elif 89 >= score >= 60:
    degree = 'B'
elif score< 60:
    degree = 'C'
else:
    degree = '分数输入错误'
    print('分数输入不符合要求，请重新输入')

print('根据这个分数得出，您的等级为：', degree)

