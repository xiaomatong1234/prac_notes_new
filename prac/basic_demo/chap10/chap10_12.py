"""
练习10-12：记住喜欢的数　
将练习10-11中的程序合二为一。
如果存储了用户喜欢的数，就向用户显示它，否则提示用户输入喜欢的数并将其存储到文件中。
运行这个程序两次，看看它能否像预期的那样工作。

"""
import json

filename = 'favorite_num.json'
try:
    with open(filename,'r') as f:
        content = f.read().strip()
        if not content:
            raise ValueError('File is empty.')
        num = json.loads(content)
except FileNotFoundError:
    num = int(input('Please enter a number：'))
    with open(filename, 'w') as f:
        json.dump(num, f) # type: ignore
    print("Thanks, I'll remember that.")
except ValueError:
    num = int(input('File is empty.Please enter a number：'))
    with open(filename, 'w') as f:
        json.dump(num, f) # type: ignore
    print("Thanks, I'll remember that.")
else:
    print(f"I know your favorite number! It's {num}.")




