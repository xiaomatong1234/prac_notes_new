import time

# count_time 创建必包的函数
def count_time(func):
    def inner():
        print("start")
        start_time = time.time()
        func()# 闭包 引用的外部函数是一个变量
        stop_time = time.time()
        print(f'函数执行时间为{stop_time - start_time}秒')
        print("end")
    return inner

@count_time
def show():
    for i in range(3):
        print(f"第 {i+1} 次输出")
        time.sleep(1)

if __name__ == '__main__':
   # @count_time 与 show = count_time(show)等价

    show()
    # show()


# 结果：
# 第 1 次输出
# 第 2 次输出
# 第 3 次输出
# 函数执行时间为3.0111730098724365秒
