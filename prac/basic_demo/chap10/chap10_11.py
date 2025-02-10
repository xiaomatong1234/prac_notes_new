"""
练习10-11：喜欢的数　
编写一个程序，提示用户输入喜欢的数，并使用json.dump()将这个数存储到文件中。
再编写一个程序，从文件中读取这个值，并打印如下所示的消息。
I know your favorite number!It's _____.
"""
import json

filename = 'favorite_num.json'
num = input('Enter a you favorite number: ')

with open(filename, 'w') as json_file:
    json.dump(num, json_file)
    print("Thanks! I'll remember that.")

with open(filename, 'r') as f:
    num = json.load(f)
    print('I know your favorite number:', num)


