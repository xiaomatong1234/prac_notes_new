"""
练习10-5：调查　
编写一个while循环，询问用户为何喜欢编程。
每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
"""
# filename = 'cause.txt'
# causes = []
# while True:
#     cause = input('Why do you like programming：')
#     causes.append(cause)
#     if cause == 'exit':
#         print('退出当前运行的程序！！')
#         break
#
# with open(filename, 'a') as f:
#     for cause in causes:
#         f.write(f'{cause}' + '\n')





filename = 'programming_poll.txt'
responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)
    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

    with open(filename, 'a') as f:
        for response in responses:
            f.write(f"{response}\n")



