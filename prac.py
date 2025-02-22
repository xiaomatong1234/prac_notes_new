"""斐波那契+1"""
# def fibonacci(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2) +1
#
#
# for i in range(10):
#     print(fibonacci(i),end=' ')



# def get_number():
#     num = input('请输入一个数字：')
#     return int(num)
#
#
# print('hello' * get_number())

# def fac(n):
#     if n==0 or n==1:
#         return 1
#     return fac(n-1) * n


# print(fac(5))

# def fac2(n):
#     result = 1
#     while n > 0:
#         result *= n
#         n -= 1
#     return result
#
#
# print(fac2(5))

# def rev(s):
#     if len(s)==0:
#         return ' '
#     return s[-1] + rev(s[:-1])
# string = 'hello'
# print(rev(string))

# arr = [1,2,3,4,5]
# result = 0
# for i in arr:
#     result +=i
# print(result)

# def lst(a):
#     result = 0
#     for i in a:
#         result += i
#     return result
#
# arr = [1, 2, 3, 4, 5]
# print(lst(arr))


# def lst(arr):
#     if len(arr) == 0:
#         return 0
#     return arr[-1] + lst(arr[:-1])
# arr =[1,2,3,4,5]
# print(lst(arr))
# def string(arg):
#     if len(arg) == 0:
#         return ""
#     return arg[-1] + string(arg[:-1])
# arga = 'hello'
# print(string(arga))
# 'o hell'
# 'l hel'
# 'l he'
# 'e h'
# 'h'
# ''
def fibo(n):
    # if n==0:
    #     return
    # elif n==1:
    #     return [1]
    # elif n==2:
    #     return [1,1]
    # f_lst = fibo(n-1)
    # f_lst.append(f_lst[-1]+f_lst[-2])
    # return f_lst
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

for i in range(1,4):
    print(fibo(i),end=" ")
"""
f(4)=fibo(3)+fibo(2)  2+1 
f(3)=fibo(2)+fibo(1)  1+1  
f(2)=fibo(1) +fibo(0) 1+0
f(1)=1           
f(0)=0

1,1,2,3,5
"""
# fibo(3)+fibo(2) 5
# fibo(2)+fibo(1) 3
# fibo(1)+fibo(0) 1
# fibo(0) 0

# [1,1,2,3,5]