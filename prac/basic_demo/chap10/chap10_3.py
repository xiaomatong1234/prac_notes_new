"""
练习10-3：访客　
编写一个程序，提示用户输入名字。用户做出响应后，将其名字写入文件guest.txt中。
"""
user_name =  input('请输入姓名：')
filename = "guest.txt"

with open (filename,'w') as f:
    print(f.write(user_name))
f.close()
