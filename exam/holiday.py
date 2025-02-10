"""1.24"""
# def num_lst():
#     for i in lst1:
#         if i in lst2:
#             return True
#         return False
#
# lst1 = [7,8,1]
# lst2 = [2,3,5]
#
# print(num_lst())
"""1.25"""
# def numbers(nums,n):
#     # 创建一个空列表，用来存储偶数
#     lst = []
#     # 遍历原始列表nums,找出所有的偶数
#     for num in nums:
#         if num % 2 == 0:
#             lst.append(num)
#     # 取出最后的第n个偶数
#     if n > len(lst):
#         return lst
#     else:
#         return lst[-n:] # 返回最后n个偶数
#
#     # for i in range(len(nums)):
#     #     if i >= n:
#     #         if nums[i] % 2 == 0:
#     #             lst.append(nums[i])
#     # return lst
#
# # nums = [1,2,3,4,5,6,7,8,9]
# # nums = [-22,5,3,11,26,-6,-7,-8,-9,-8,26]
# nums = [6,-25,3,7,5,5,7,-3,23]
#
# print(numbers(nums, 1))
"""1.26"""
# def big_age():
#     for i in range(len(nums)):
#         for j in range(len(nums)-1-i):
#             if nums[j] > nums[j+1]:
#                nums[j], nums[j+1] = nums[j+1], nums[j]
#     return nums[-2:]
#
# nums = [1,3,10,0]
# print(big_age())
"""1.27"""
"""
1001001001001001
2 2
3 4
4 6
5 8
6 10
7 12
"""
"""2个蓝珠子之间夹着连续的两个红色珠子"""
# def blue_num():
#     if num < 2:
#         return 0
#     else:
#         return (num - 1)*2
# num = int(input('请输入蓝色珠子的数量：'))
# print('红色珠子的数量为：',blue_num())
"""1.28"""
#
# def account():
#     # 提取列表中的数字的个、十、百位
#     num1 = nums[0] // 100
#     num2 = nums[0] % 100 // 10
#     num3 = nums[0] % 10
#     # print(num1, num2, num3)
#
#     num1_1 = nums[1] // 100
#     num2_1 = nums[1] % 100 // 10
#     num3_1 = nums[1] % 10
#     # print(num1_1, num2_1, num3_1)
#
#     # 交换百位的位置
#     num4 = num1
#     num1 = num1_1
#     num1_1 = num4
#
#     # 将个位、十位、百位拼接到一起
#     result1 = f"{num1}" + f"{num2}" + f"{num3}"
#     result2 = f"{num1_1}" + f"{num2_1}" + f"{num3_1}"
#       计算差值的绝对值
#     result = f'{result1} - {result2} ='
#     print(result,abs(int(result1)-int(result2)))
# nums = [523,456]
# account()



# def account():
#     # 提取百位、十位、个位
#     num1, num2 = nums
#     num1_swapped = (num2 // 100) * 100 + (num1 % 10) * 10 + (num1 // 10 % 10)
#     num2_swapped = (num1 // 100) * 100 + (num2 % 10) * 10 + (num2 // 10 % 10)
#
#     # 计算差值的绝对值
#     result = abs(num1_swapped - num2_swapped)
#
#     # 打印结果
#     print(f"{num1_swapped} - {num2_swapped} = {result}")
#
# # 示例输入
# nums = [223, 456]
# account()
"""2.2"""
# def total_space(num_lst):
#     # 先对列表排序
#     num_lst.sort()
#     # 定义起点、终点的初始值
#     current_start,current_end = num_lst[0]
#     # 计算间距
#     total_distance = 0
#     for start,end in num_lst:
#         # 如果当前区间与前一个区间重叠，更新current_end
#         if start <= current_end:
#             current_end = end
#         else:
#             # 如果不重叠，累加之前区间的长度，并更新current_start和current_end
#             total_distance += current_end - current_start
#             current_start,current_end = start,end
#     # 最后一个区间的长度
#     total_distance += current_end - current_start
#     return total_distance
#
# num_lsts = [(1,2),(7,10),(7,10)]
# print(total_space(num_lsts))
"""2.3"""
# def extremum(num):
#     # 分别取出百、十、个位的数字
#     bit = num // 100
#     ten_bit = num // 10 % 10
#     hundred = num % 10
#
#     if hundred >= ten_bit > bit and hundred > bit:
#         bit,ten_bit,hundred = hundred,ten_bit,bit
#
#     print(bit,ten_bit,hundred,sep='')
#
# number = int(input('请输入一个数字：'))
# extremum(number)

"""2.4"""
def typist(word):
    length = 0
    caps_lock_on = False
    for letter in word:
        if letter.isupper():
            if not caps_lock_on:
                length += 1
                caps_lock_on = True
            length += 1
        else:
            if caps_lock_on:
                length += 1
                caps_lock_on = False
            length += 1

    print(length)

words = str(input('输入字母，统计员工敲击键盘的次数：'))

typist(words)


















