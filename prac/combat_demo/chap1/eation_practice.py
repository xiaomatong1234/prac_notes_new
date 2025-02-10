# """编写一个以句子（字符串）为输入内容的python脚本程序，该程序会返回一个字符型的简单条形图"""
import pprint
from collections import defaultdict

# 输入一个句子
sentence = str(input('Enter a sentence:'))
# 定义一个空字典接收
# 使用defaultdict来避免手动检查健是否还存在
dic = defaultdict(int)
# 遍历整个句子
for char in sentence:
    if char.isalpha():
        if char.lower()not in dic:
            dic[char] = 1
        else:
            dic[char] += 1
# # 输出字符频率
# pprint.pprint(dic)

# 遍历整个字典
for char, count in dic.items():
    print(f'{char}: {char * count}')
    # lst = char*count
    # pprint.pprint(f'{char}:{lst}', width=120)

# """Map letters from string into dictionary & print bar chart of frequency."""
# import sys
# import pprint
# from collections import defaultdict
#
# # Note: text should be a short phrase for bars to fit in IDLE window
# text = 'Like the castle in its corner in a medieval game, I foresee terrible \
# trouble and I stay here just the same.'
#
# ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
#
# # defaultdict module lets you build dictionary keys on the fly!
# mapped = defaultdict(list)
# for character in text:
#     character = character.lower()
#     if character in ALPHABET:
#         mapped[character].append(character)
#
# # pprint lets you print stacked output
# print("\nYou may need to stretch console window if text wrapping occurs.\n")
# print("text = ", end='')
# print("{}\n".format(text), file=sys.stderr)
# pprint.pprint(mapped, width=110)
