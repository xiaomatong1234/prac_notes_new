"""
练习10-4：访客名单　
编写一个while循环，提示用户输入名字。
用户输入名字后，在屏幕上打印一句问候语，并将一条到访记录添加到文件guest_book.txt中。
确保这个文件中的每条记录都独占一行。
"""
filename = 'guest.txt'
while True:
    user_name = input('Enter your name: ')
    if user_name == 'q':
        print('退出当前程序！')
        break
    else:
        with open (filename,'a') as f:
            f.write(user_name + '\n')
            print('Hello', user_name)

