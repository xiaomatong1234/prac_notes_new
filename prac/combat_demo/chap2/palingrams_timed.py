import time

import load_dictionary

#
# start_time = time.time()
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
start_time = time.time()
palingrams = find_palingrams()
end_time = time.time()
print(f'Runtime for this program is:{end_time - start_time} seconds.')

palingrams_sorted = sorted(palingrams)

# 输出回文短句列表
print('Number of palingrams:', len(palingrams_sorted))
for first,second in palingrams_sorted:
    print(f'{first},{second}')

# end_time = time.time()
# print(f'Runtime for this program is:{end_time - start_time}seconds.')
