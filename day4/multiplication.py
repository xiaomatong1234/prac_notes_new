# 九九 乘法表
def multiplication():

    for i  in range(1, 10): # 外层循环 控制列
        for j in range(1, i+1): # 内层循环 控制行
            if j <= i :  #
                print(f'{j}*{i}={i * j:<2}',end=' ')  # :<2 左对齐 输出2宽度的数字
        print()

print("----九九 乘法表---")
if __name__ == '__main__':
    multiplication()





