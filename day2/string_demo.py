# s1 = "hello\t hogwarts \"world\"\n"
# s2 = "hello\t hogwarts\\ \'world\'"
# print(s1,s2)
# # 取
# # print('取字符串中的第3个字母',s1[90])
# #统计字符串的长度
# length = len(s2)
# print(length)
# #  统计子zi fu chuan
# num_l = s2.count("l")
# print(num_l)
#
# #
# num_l1 = s1.count("l", 0, 5)
# print(num_l1)
#
# index_l = s2.index('l')
#
# s = 'Hello Hello Hello Hello Hello Hello Hello Hello Hello'
# new_s = s.replace('ll', 'LL', 90)
# print(new_s)

url = "https://www.ceshirencom "

# #判断字符串是否以某一个子字符串
# print(url.startswith("https://"))
# print(url.endswith(".com1"))
# # 判断字符串不为空，并且包含的全是字母
# print(url.isalpha())
# # 判断字符串不为空，并且包含的都是数字
# print(url.isdigit())
# # 判断字符串不为空，并且包含的是字母或者数字
# print(url.isalnum())
# # 判断字符串中只包含空格类内容
# print(url.isspace())
# # 判断字符串中都是包含的大写字母
# print('AAAfAA'.isupper())
# # 判断字符串中都是小写的字母
# print('判断字符串中都是小写的字母：','sdss'.islower())
# print('判断所有单词的首字母大写：')
# # 填充字符
# 删除啊字符串左右两侧的空白字符
# print("bbbahogcwabbbrtsbcba".strip("cba"))
# 使用换行符分割字符串
# print('a\nb')
# #连接可迭代对象生成
# l1 = '-'.join(("a","b","c","d"))
# print(l1)
# print(l1.split('-'))
# 字符串的解码和编码
# print("1232323".encode('utf-8'))
# s2  = b'1232323'
# print(s2.decode('gb2312'))
'''
编写一个Python程序，输入一个5位数，判断输入的这个数字是否为回文数。
回文数是指从左到右和从右到左读都一样的数。例如12321。
如果输入的是回文数，输出是回文数，否则输出不是回文数
'''
# num = input('请输入5位数：').strip()
# # 75257   0 1 2 3 4
# num1 = num[0]
# num2 = num[4]
# num3 = num[1]
# num4 = num[3]
#
# print('第1位数：', num1)
# print('第5位数：', num2)
# print('第2位数：', num3)
# print('第4位数：', num4)
#
# if num1 == num2:
#     print('第一位数和第五位数一样，程序可以继续!')
#     if num3 == num4:
#         print('第二位数和第四位数一样，当前数字输入符合要求！！')
#     else:
#         print('第二位数和第四位数不一样，不符合要求~~~')
# else:
#     print('第一位数和第五位数不一样，不符合要求~~~')
#
# print('当前输入的五位数字为：', num.strip())
#
# story = "Once upon a time, in a land far away, lived a brave knight named Arthur."
# print(f'{story}单词数量:', len(story.split()))
# print('主人公名字的位置为：', story.find('Arthur'))
# print('替换名字：',story.replace('Arthur', 'tangyuan'))
# print('将故事改为大写：', story.upper())
# print('将故事改为小写：', story.lower())

# s= ['Hello', 'Hello']
# # print(s[-3: -1])
# # print(s[::-1])
# # print(s[1:5:3])
# a = len(s)
# print(a)

# story = "Once upon a time, in a land far away, lived a brave knight named Arthur."
# #统计故事中单词的数量
# list1 = story.split()
# print(list1)
# print(len(list1))
a ,b = 1,2
b,a = a,b
print(a,b)