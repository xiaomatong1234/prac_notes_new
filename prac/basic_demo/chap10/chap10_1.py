filename = "learning_python.txt"
"""第一次打印时读取整个文件"""
with open(filename) as f:
    print(f.read())

"""第二次打印时遍历文件对象"""
with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

"""第三次打印时将各行存储在一个列表中，再在with代码块外打印它们"""
with open(filename) as f:
    lines = f.readlines()
for line in lines:
    print(line.strip())
