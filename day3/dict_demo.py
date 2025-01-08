#   key=value  key会转成字符串，value类型不变
d1 = dict(one=1, two=2, three=3)
print(d1)

# 列表 是可迭代对象
#
d7 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(d7)
# 获取字典中的值
stu = {"name":"Tom", "age": 23, "gender":"male"}
print(stu["name"])
print(stu["age"])

# 字典中新增数据
stu['school'] = "hogwarts"
print(stu)
# 修改字典中已存在的数据
stu['school'] = 'tangyuan'
print(stu)

# 删除字典中的元素
del stu['school']
print(stu)

# 取字典中所有的 key
print(stu.keys())

# 取字典中所有的 value
print(stu.values())

# 获取字典中所有的键值对
print(stu.items())

# 通过key获取值
# print(stu['school']) 获取 key 对应的值不存在会报错
print(stu.get("school"))
print(stu.get("name"))
print(stu.get("school", '获取 key 对应的值不存在'))

# 更新字典 将不存在的值
print(stu.setdefault('address'))
print(stu)
# 使用可迭代对象(元祖、列表)作为key 去生成字典
keys = {"name", "age","gender"}
d6 = dict.fromkeys(keys, "无无")
print(d6)

# 合并两个字典
d_new = {
    "city" : "peking",
    "address": "西二旗"
}

d6.update(d_new)
print(d6)

# 更新一个可迭代的对象进入字典
new_info = [("hobby","sing"),("pet", 'cat')]
d6.update(new_info)
print(d6)

# 删除字典中最后一个jianzhi对
print(d6.popitem())
print(d6)

# 删除指定的key
print(d6.pop('city'))
print(d6)

# 清空所有键值对
print(d6.clear())
print(d6)