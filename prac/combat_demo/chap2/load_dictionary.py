"""
以列表的形式加载一个文本文件
参数：文本文件的名字
异常：如没有找到文件，则报告IOError类型的异常
返回值：一个包含文本文件中所有小写形式的列表
要求导入的模块sys
"""
import sys
def load(filenames):
    try:
        with open(filenames) as file:
            loaded_txt = file.read().strip().split('\n')
            # 列表推导，将所有的单词转换为小写
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f"\n Error opening file:{filenames}", e, file=sys.stderr)
        sys.exit(1)

filename = "file.txt"
# print(load(filename))





