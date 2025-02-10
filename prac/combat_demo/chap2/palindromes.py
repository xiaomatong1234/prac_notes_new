"""
以列表的形式在字典文件中的单词
创建一个空列表，保存查找的回文单词
循环遍历列表中的每个单词：
    如果单词的正向切片与反向切片相同：
        将该单词添加到回文单词列表中
输出回文单词列表
"""
import load_dictionary

word_lst = load_dictionary.load('file.txt')
pali_lst = []
for word in word_lst:
    if len(word)>1 and word == word[::-1]:
        pali_lst.append(word)

print('Number of empty words:', len(pali_lst))
print('\n'.join(pali_lst))
# print(empty_lst)


