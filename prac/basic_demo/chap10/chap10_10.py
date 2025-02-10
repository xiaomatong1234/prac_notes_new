"""人"""
def book(filename,word):
    try:
        with open(filename,'r',encoding='utf-8') as f:
            contents = f.read()
            # print(contents)
    except FileNotFoundError:
        pass
    else:
        word_nums = contents.count(word)
        print(word_nums)

filenames = 'swear_word.txt'
book(filenames,'人')