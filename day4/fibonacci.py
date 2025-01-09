'''
实战：for 循环实现斐波那契
编写一个 Python 程序，使用 for 循环，生成并输出斐波那契数列的前 n 项,其中 n 是用户指定的正整数。

斐波那契数列，又称黄金分割数列，指的是：1、1、2、3、5、8、13、21、34....从第三个数开始，每个数字都是前两个数字之和。
1, 2, 3, 4, 5, 6, 7
1, 1, 2, 3, 5, 8, 13

递归
'''
def fibonacci(n):
    if n<=0:
        return []
    # 用户输入1，返回[1]
    elif n == 1:
        return [1]
    # 用户输入2，返回[1,1]
    elif n == 2:
        return [1,1]

    # 用户输入其它数字,应返回[1,1,...,n]
    else:
        # 定义一个列表
        fibs = [1,1]
        # 计算出需要加入列表中的数字
        # for i in range(2, n):  #[0,1,2] i=3  (2,3)

        for _ in range(2, n):  # 将i优化为_
            # next_num = fibs[i-1] + fibs[i-2] #i=3, 2-1=1,2-2=0
            fibs.append(fibs[-1] + fibs[-2]) #优化减法操作 fibs[-1] 列表的最后一项，fibs[-2]列表的倒数第二项
        return fibs

# 用户输入的正整数
n = int(input('用户输入的正整数为：'))
if __name__ == '__main__':
    print(fibonacci(n))

