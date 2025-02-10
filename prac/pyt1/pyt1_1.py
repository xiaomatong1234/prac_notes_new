"""九九乘法表"""
# for i in range(1,10):
#     for j in range(1,10):
#         if j <= i:
#             print(f'{j} * {i} = ' f'{i * j:<2}', end='  ')
#     print(' ')

for i in range(1,10):
    for j in range(1,i+1):
        print('{0}*{1} ={2}'.format(j, i, j*i), end=' ')
    print('')
