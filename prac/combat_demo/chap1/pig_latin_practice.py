"""
儿童黑话
"""
# # 用户输入一个单词

words = input("Enter a word: ")
lst = words.split()

# 判断单词是以原音开头，还是以辅音开头
# 原音a e i o u
# 单词以元音开头，在单词后面加上“way”
for word in lst:
    if word[0].lower() in 'aeiou':
        print(word + 'way', end=' ')
    # 如果单词以辅音字母开头
    else:
        # 单词以辅音开头，把辅音移至末尾，在末尾加上“ay”
        print(word[1:] + word[0] + "ay", end=' ')





