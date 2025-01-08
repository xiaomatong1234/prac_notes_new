'''
实战代码
编写一个 Python 程序，来计算给定文本中每个单词出现的次数。
text = """
Python is a popular programming language. It is widely used for web development, data science, and more.
Python has a simple and readable syntax, which makes it great for beginners.
"""
'''


text = """
Python is a popular programming language. It is widely used for web development, data science, and more.
Python has a simple and readable syntax, which makes it great for beginners.
"""

# 拆分单词
word1 = text.lower().replace("," , " ")
word2 = word1.replace(".", " ").split()
print('拆分后的单词为：', word2)

# 遍历当前列表，并把每个单词打印出来
word_count = {}
for w in word2:
    print( w)
#    完成单词的统计
    if w in word_count:
        # 如果单词已经在统计字典中，那么单词出现次数+1
        word_count[w] += 1
    else:
        word_count[w] = 1
# 打印最终统计结果
print(word_count)

# 打印统计字典中key和value的值
for k,v in word_count.items():
    print(f'{k}: {v}')









