# 待排序的数据
students = [
    {'name': 'Alice', 'id': '1001', 'class': 'Class1'},
    {'name': 'Eve', 'id': '1005', 'class': 'Class2'},
    {'name': 'Charlie', 'id': '1003', 'class': 'Class1'},
    {'name': 'David', 'id': '1004', 'class': 'Class2'},
    {'name': 'Bob', 'id': '1002', 'class': 'Class1'},
    {'name': 'Frank', 'id': '1006', 'class': 'Class2'}
]
# TypeError: '<' not supported between instances of 'dict' and 'dict'
# students.sort()


# 以名字排序
students.sort(key=lambda stu: stu["name"] + stu["id"])

def sort_by_name(student):
    return student["name"] + student["id"]

# 以ID降序排序
students.sort(key=sort_by_name)
for s in students:
    print(s)


def test_filter():
    a=[1,2,3]
    r = filter(lambda x:x>2, a)


def test_filter():
    a=[1,2,3]
    r = filter(lambda x:x>2, a)
    print(list(r))