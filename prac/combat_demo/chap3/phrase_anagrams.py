import sys
from collections import Counter

from prac.combat_demo.chap3 import load_dictionary


dic_file = load_dictionary.load('file.txt')
dic_file = sorted(dic_file)

ini_name = input('请输入英文短语：')

# 寻找易位词
def find_anagrams(name, word_lst):
    """根据用户输入的名字，在字典中寻找易位短语，输出最终找到的易位短语"""
    name_letter_map = Counter(name)
    anagrams = []

    for word in word_lst:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word_letter_map:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == Counter(word):
            anagrams.append(word)
    print(*anagrams, sep='\n')
    print()
    print(f"剩余字母 = {name}")
    print(f"剩余字母数量 = {len(name)}")
    print(f"dic_file字典中匹配的单词数量 = {len(anagrams)}")


# 处理用户选择
def process_choice(name):
    """检查用户输入的有效性，返回用户所做的选择及输入名字中剩余的字母"""
    while True:
        candidate = '' # 用户选择输入的名字
        choice = input('请选择剩余字母，或摁#退出，或摁回车键重新生成剩余字母：')
        if choice == '#':
            sys.exit()
        elif choice == '':
            main()
        else:
            candidate = ''.join(choice.lower().split())

        left_over_lst = list(name) # 将输入的短语该换成列表
        for letter in candidate:
            if letter in left_over_lst:
                left_over_lst.remove(letter)

        if len(name) - len(left_over_lst)  == len(candidate):
            break
        else:
            print('选择的单词不在剩余的英文短语中，请重新选择！！',file=sys.stderr)
    name = ''.join(left_over_lst)
    return choice, name
    # print(f'已输入的短语中剩余的单词为：{name}')

# 定义main函数
def main():
    """根据用户输入的名字生成易位短语"""
    name = ''.join(ini_name.lower().split())
    name = name.replace('_', '')
    limit = len(name)
    phrase = '' # 用户选择完成后生成的易位短语

    running = True
    while running:
        temp_phrase = phrase.replace(' ', '')
        if len(temp_phrase) < limit:
            print(f'用户选择完成后，生成易位短语的长度为：{len(temp_phrase)}')
            find_anagrams(name, dic_file)
            print(f'生成的易位短语为：{phrase}')

            choice,name = process_choice(name)
            phrase += choice + ' '

        elif len(temp_phrase) == limit:
            print('*'*10,'FINISHED!!!','*'*10)
            print(f'易位短语为：{phrase}')
            print()

            try_again = input('\n\n想要再次尝试吗？y/n')
            if try_again == 'y':
                main()
            else:
                running = False
                sys.exit()


if __name__ == '__main__':
    main()






# find_anagrams(ini_name,dic_file)
# process_choice(ini_name)