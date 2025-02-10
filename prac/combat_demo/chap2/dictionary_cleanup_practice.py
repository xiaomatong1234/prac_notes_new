import time

import load_dictionary

#
# start_time = time.time()
word_lst = load_dictionary.load("file.txt")


def find_palingrams():
    pali_lst = []
    words = set(word_lst)
    for word in words:
        end = len(word)
        res_word = word[::-1]
        if len(word) > 1:
            for i in range(end):
                # 检查尾部与反转部分匹配
                if word[i:] == res_word[:end-i] and res_word[end-i:] in words:
                    # print(f'Found pali pair:( {word},{res_word[end-i:]})')
                    pali_lst.append((word, res_word[end - i:]))

                # 检查头部与反转部分匹配
                if word[:i] == res_word[end-i:] and res_word[:end-i] in words:
                    # print(f'Found res_pali pair:( {res_word[:end - i]},{word})')
                    pali_lst.append((res_word[:end - i], word))

        # for p in pali_lst:
        #     if len(p)==1:
        #         pali_lst.remove(p)
    # 过滤掉单个字母单词构成的回文短语
    pali_lst = [p for p in pali_lst if len(p[0]) > 1 and len(p[1]) > 1]
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
