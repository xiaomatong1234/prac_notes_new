"""
练习：个性化消息 用变量表示一个人的名字，并向其显示一条消息。显示的
消息应非常简单，下面是一个例子
Hello Eric, would you like to learn some Python today?
"""
name = 'Eric'
message = f'Hello {name}, would you like to learn some Python today?'
print(message)

"""
练习 2-4：调整名字的大小写 用变量表示一个人的名字，再以小写、大写和首字
母大写的方式显示这个人名。
"""
# 名字首字母大写
name = name.title()
message1 = f'Hello {name}, would you like to learn some Python today?'
print(message1)

# 名字大写
name = name.upper()
message2 = f'Hello {name}, would you like to learn some Python today?'
print(message2)

# 名字小写
name = name.lower()
message3 = f'Hello {name}, would you like to learn some Python today?'
print(message3)

"""
练习 2-5：名言 找一句你钦佩的名人说的名言，将其姓名和名言打印出来。输出
应类似于下面这样（包括引号）。
Albert Einstein once said, “A person who never made a mistake never tried anything new.”
"""
famous_name = 'Thomas Carlyle'
famous_saying = 'Cease to struggle and you cease to live.'
mes = f'{famous_name} say, "{famous_saying}"'
print('名人名言：',mes)

"""
练习 2-6：名言 2 重复练习 2-5，但用变量 famous_person 表示名人的姓名，再创
建要显示的消息并将其赋给变量 message，然后打印这条消息。
"""

"""
练习 2-7：剔除人名中的空白 用变量表示一个人的名字，并在其开头和末尾都包
含一些空白字符。务必至少使用字符组合"\t"和"\n"各一次。
打印这个人名，显示其开头和末尾的空白。然后，分别使用剔除函数 lstrip()、
rstrip()和 strip()对人名进行处理，并将结果打印出来。
"""
person_name = '    Thomas Carlyle  '
person_name1 = '   \tThomas Carlyle\n'
# rstrip 删除后面的空格
person_name = person_name.rstrip()
person_name1 = person_name1.rstrip()
print('删除后面的空格：',f'{person_name}')
print('删除后面的空格：',f'{person_name1}')

# lstrip 删除前面的空格
person_name = person_name.lstrip()
person_name1 = person_name1.lstrip()
print('删除前面的空格：',f'{person_name}')
print('删除前面的空格：',f'{person_name1}')

# strip 删除前后的空格
person_name = person_name.strip()
person_name1 = person_name1.strip()
print('删除前后的空格：',f'{person_name}')
print('删除前后的空格：',f'{person_name1}')

# print(f'{person_name}{person_name1}')

name = "\tEric Matthes\n"
print("Unmodified:")
print(name)
print("\nUsing lstrip():")
print(name.lstrip())
print("\nUsing rstrip():")
print(name.rstrip())
print("\nUsing strip():")
print(name.strip())




