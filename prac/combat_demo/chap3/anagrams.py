"""
以列表的形式加载字典文件中的内容
获取用户输入的单词
创建一个用于保存易位单词的空列表
对用户输入的单词进行排序
循环遍历列表中的每个单词:
    对取出的单词排序
    如果所取出的单词排序结果与用户输入单词的排序结果相同:
        将这个单词添加至易位词列表
输出易位词列表
"""
import sys

from prac.combat_demo.chap2 import load_dictionary

filename = '/Volumes/software/warehouse/python_practice/python_prac0107/prac/combat_demo/chap2/file.txt'
word_lst = load_dictionary.load(filename)

def anagrams():
    anagram_lst = []
    name = input('请输入一个单词：')
    print(f'Input name = {name}')
    # 将输入单词转换为小写
    name = name.lower()
    print(f'Use name = {name}')
    # 排序用户输入的单词
    name_sorted = sorted(name)
    # 遍历字典中的每个单词
    for word in word_lst:
        # 对字典中的每个单词排序
        word_sorted = sorted(word)
        # 如果排序后的单词相同，说明是易位词
        if word_sorted == name_sorted:
            anagram_lst.append(word)

    # 输出易位词列表
    if not len(anagram_lst):
        print('You need a larger dictionary or a new name!', file=sys.stderr)
    else:
        print('Anagrams=',sep='\n')
        # 使用 join() 将结果打印在一行，每个单词之间换行
        print("\n".join(anagram for anagram in anagram_lst))

if __name__ == '__main__':
    anagrams()
