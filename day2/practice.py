'''
统计查找替换类
# len(obj)  获取参数字符串的个数   通用函数
# count(str,start,end)  在start,end范围内，str在string中出现的次数 字符串的对象来调用
# index(sub,start,end)) 在start,end范围内，检测sub是否包含在string中，若包含返回索引值，否则报错
# find(sub, start, end) 在start,end范围内，检测sub是否包含在string中，若包含返回开始的索引值，否则返回-1
# replace(old, new, max) 把string中的old替换成new, max指定替换次数
'''
# len(obj)  获取参数字符串的个数   通用函数
length = "Hello"
print(f'当前{length}长度为：', len(length))

# count(str,start,end)  在start,end范围内，str在string中出现的次数 字符串的对象来调用
s1 = "helloworldhelloPython"
a = s1.count('hello')
print(f'在[{s1}]中hello出现的次数是：', a)
b = s1.count('o', 4,8)
print(f'在【{s1}】中o出现的次数是：', b)

# index(sub,start,end)) 在start,end范围内，检测sub是否包含在string中，若包含返回索引值，否则报错
s2 = "Hello 12345"
try:
    c = s2.index('1', 0, 3)
    print(c)
except:
    print('ValueError: substring not found')

# find(sub, start, end) 在start,end范围内，检测sub是否包含在string中，若包含返回开始的索引值，否则返回-1
s3 = "hello-123, 34-5-, 234"
d = s3.split('-',2)
# d1 = d.find('3', 0, 2)
print(d)
e = s3.find('l', 0, 3)
print(e)

# replace(old, new, max) 把string中的old替换成new, max指定替换次数
s4 = 'Hello Hello Hello'
print(s4.replace('ll', 'PP', 2))

'''
字符串判断类
'''
# startswith(prefix, start, end)  在start, end区间内，判断字符串是不是以prefix开头，是返回True,否则返回False

url = "https://www.ceshiren.com"
print(url.startswith('https', 0, 4))

# endswith(suffix, start, end)  在start, end区间内，判断字符串是不是以suffix结尾，是返回True,否则返回False
print(url.endswith('.com', 20,24))

# isalpha() string 至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False 有空格也会返回fale
print(s1.isalpha())

# isdigit() 如果 string 只包含数字则返回 True 否则返回 False
s5 = '12345'
print(s5.isdigit())


