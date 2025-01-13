"""
实战代码
创建一个类 Library，实现以下功能：
类属性：记录总书籍数量与当前借出的书籍数量。
类方法：
获取当前的书籍状态（总书籍数量、已借出书籍数量、可借书籍数量）。
修改总书籍数量（如新增书籍）。
实现实例方法，用于借书和还书的操作，并同步更新类属性。
模拟图书借阅操作，验证类属性和类方法的正确性。
"""
class Library:
    """图书馆类"""
    # 类属性 记录总书籍数量与当前借出的书籍数量
    total_books = 100
    borrow_books = 0

    @classmethod
    def get_books_status(cls):
        # 获取当前书籍状态
        can_borrowed = cls.total_books - cls.borrow_books

        return cls.total_books, cls.borrow_books

    @classmethod
    # 访问类属性 类方法中获取类属性的值 新书籍的数量
    def add_books(cls, num):
        cls.total_books += num
        return cls.total_books


# 使用类方法 对类属性访问
print(f'总书籍数量为：{Library.total_books}')
print(f'已借出书籍数量为：{Library.borrow_books}')
print(f'可借出书籍数量为：{Library.get_useful_books()}')

# 创建对象
book1 = Library()
book2 = Library()
print(f'实例化两次后，总书籍数量为：{Library.total_books}，已借出书籍数量为{Library.borrow_books}，可借出书籍数量为{Library.get_useful_books()}')

Library.get_books_status()
# 修改总书籍数量之后，总书籍的数量
print(f'修改总书籍数量之后，总书籍的数量为：{Library.get_books_status()}')