"""
练习9-14：彩票　
创建一个列表或元组，其中包含10个数和5个字母。
从这个列表或元组中随机选择4个数或字母，并打印一条消息，指出只要彩票上是这4个数或字母，就中大奖了。
"""
from random import choice
lst = ["1","2","3","4","5","6","7","8","9","10",'a','b','c','d','e']
results = []
while len(results) < 4:
    result = choice(lst)
    if result not in results:
        results.append(result)
print('中大奖了：', results)

