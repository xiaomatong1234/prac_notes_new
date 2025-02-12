l1 = []

l2 = [1,2,3,True,[1,2,3,4]]
# print(type(l1),type(l2))
#
# l3 = list("abc")
# print(l3)
# # 通过索引访问列表中的元素
# b = l2[1:4:1]
# print(b)
# # 修改
# l2[3] = False
# print(l2)
# # 列表的切片操作
# print(l2[:3])
# # 从第二个开始切到最后
# print(l2[1:])
# # 倒序
# print(l2[::-1])
# print(len(l2))
# # 统计列表中指定元素出现的次数
# print(l2.count(2))
# #查找3第一次出现的位置
# print(l2.index(3))
# # 向列表中追加内容
# l1.append('abc')
# print(l1)
# l1.append(123)
# print(l1)
# l1.extend('jjkl')
# print(l1)
# l1.extend((1,2,3))
# print(l1)
# l1.extend(["123",456])
# print(l1)
# l1.insert(0,'123213213')
# print(l1)
# del l1[0]
# print(l1)
# l1.remove(1)
# students.txt = [["Anna", 90], ["Tom", 78], ["Jerry", 85], ["Lucy", 92]]
# total = len(students.txt)
# print('学生总人数为：', total)
# # "Mark"（87分）和 "Eva"（80分）
#
# add_student1 = students.txt.extend([["Mark",87],["Eva",80]])
#
# print(f'打印一下学生：{students.txt}')
#
# del students.txt[1]
# print(f'当前学生数量为：{students.txt}')

'''
实战代码
管理一个书籍列表，可以实现以下功能： 
- 统计当前书籍总数。
 - 增加新书籍到列表。 
 - 删除已存在的书籍。 
 - 对书籍列表按字母顺序排序。
输出每次操作后的书籍列表和对应的提示信息。
'''
books = ["Python Programming", "Data Structures", "Artificial Intelligence", "Web Development"]
total = len(books)
print('书籍的总数为：',total)

addbook = books.extend(("java","PhP"))
print(f'新增书籍到列表：{books}', )

# # in 成员运算符
delete_book = "Artificial Intelligence"
if delete_book in books:
    books.remove(delete_book)
    print(books)
else:
    print(f'{delete_book}不在书籍列表中')

books.sort()
print(f'书籍按照字母顺序排序{books}')