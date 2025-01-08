# picture
# 打印正方形
"""
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
"""
# for i in range(5):
#     for j in range(5):
#         print("*", end="  ")
#     print()

'''
*  
*  *  
*  *  *  
*  *  *  *  
*  *  *  *  *  
# '''
print("----------------正三角----------------")
for i in range(5):
    i += 1
    for j in range(i):
        print("*", end="  ")
    print()

"""
*  *  *  *  *  
*  *  *  *  
*  *  *  
*  *  
*  
"""
print("----------------倒三角----------------")
for i in range(6,1,-1):
    i -= 1
    for j in range(i):
        print("*", end="  ")
    print()

"""
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
"""
print("----------------等腰三角----------------")

# # 打印星号
# for i in range(0,10,2):
#     i += 1
#     for j in range(i):
#         print(" ", end="  " )
#     print("*")
# 打印空格
# for i in range(9):
#     for j in range(i):
#         print("*", end="  ")
#     print('')

"""
* * * * * 
      * * *
"""
# for i in range(5):
#     for j in range(5-i-1):
#         print(" ", end=" ")
#     print("* "*(i*2+1))

for i in range(5):
    for j in range(5 - i - 1):
        print(" ", end=" ")
    print("* " * (i * 2 + 1))