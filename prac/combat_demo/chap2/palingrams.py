"""
以列表形式加载字典文件中的内容
创建一个保存回文短语的空列表
遍历列表中的每个单词:
    获取单词的长度
    如单词中每个字母大于1:
        遍历单词中的每个字母:
            如果该单词前面的字母组成倒序词，并且该单词剩余的字母构成回文序列:
                将单词及倒序词添加至回文短语列表中
            如果该单词末尾的字母组成倒序词，并且该单词前面的字母组成回文序列:
                将单词及倒序词添加至回文短语列表中
按照字母顺序对列表中的回文短语排序
输出回文短语列表中的回文单词对
"""
import load_dictionary


word_lst = load_dictionary.load("file.txt")


def find_palingrams():
    pali_lst = set() # 使用集合避免重复
    for word in word_lst:
        end = len(word)
        res_word = word[::-1]
        if len(word) > 1:
            for i in range(end):
                # 检查尾部与反转部分匹配
                if word[i:] == res_word[:end-i] and res_word[end-i:] in word_lst:
                    # print(f'Found pali pair:( {word},{res_word[end-i:]})')
                    pali_lst.add((word, res_word[end - i:]))  # 集合中添加数据使用.add

                # 检查头部与反转部分匹配
                if word[:i] == res_word[end-i:] and res_word[:end-i] in word_lst:
                    # print(f'Found res_pali pair:( {res_word[:end - i]},{word})')
                    pali_lst.add((res_word[:end - i], word))

    return pali_lst

palingrams = find_palingrams()
palingrams_sorted = sorted(palingrams)

# 输出回文短句列表
print('Number of palingrams:', len(palingrams_sorted))
for first,second in palingrams_sorted:
    print(f'{first},{second}')

