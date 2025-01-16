"""
实战代码
创建一个类 Library，
实现以下功能：
类属性：记录总书籍数量与当前借出的书籍数量。

类方法：
获取当前的书籍状态（总书籍数量、已借出书籍数量、可借书籍数量）
修改总书籍数量（如新增书籍）

实现实例方法，
用于借书和还书的操作，并同步更新类属性。
模拟图书借阅操作，验证类属性和类方法的正确性。
"""
class Library:
    # 类属性 记录总书籍数量与当前借出的书籍数量
    total_books = 100
    borrowed_books = 0

    def __init__(self,name):
        """
        构造方法 定义图书馆名称
        :param name: 图书馆名称
        """
        self.name = name

    # 类方法
    @classmethod
    def get_book_status(cls):
        """
        获取当前的书籍状态
        :return: 总书籍数量、已借出书籍数量、可借书籍数量
        """
        can_borrowed = cls.total_books - cls.borrowed_books
        book_status_info = {
            "总书籍数量": cls.total_books,
            "已借出书籍数量": cls.borrowed_books,
            "可借书籍数量": can_borrowed
        }
        return f'{lib1.name}初始书籍数量为：',book_status_info




    #类方法 修改总书籍数量（如新增书籍）
    @classmethod
    def add_books(cls,num):
        cls.total_books += num
        print(f'\n新增加了{num}本书籍，当前图书馆书籍总量为：{cls.total_books}')

    # 实例方法 借书操作
    def borrowed_book(self,num):
        """
        借书操作
        :return:
        """
        # 判断书籍总量和借书数量之间的关系
        if self.total_books > self.borrowed_books:
            self.borrowed_books += num
            self.total_books -= num
            print(f'借书成功，'
                  f'当前借出书籍数量为：{self.borrowed_books}，'
                  f'书籍总量为：{self.total_books}，'
                  f'可借书籍数量为：{self.total_books}')
        else:
            print(f'借书失败，当前可借的书籍总量为0')

    # 实例方法 还书操作
    def return_book(self,num):
        """
        还书操作
        :return:
        """
        # 判断借书数量和还书数量之间的关系
        if 0< num <= self.borrowed_books:
            self.borrowed_books -= num
            self.total_books += num
            print(f'\n还书成功，已归还{num}本书',
                f'借书成功，当前借出书籍数量为：{self.borrowed_books}，'
                f'书籍总量为：{self.total_books}，'
                f'可借书籍数量为：{self.total_books}')
        else:
            print('\n还书失败，当前归还书籍数量与借书数量不符')



# 实例Library的对象
lib1 = Library('国家图书馆')
lib2 = Library('西二旗图书馆')


# 调用get_book_status类方法
print(Library.get_book_status())

# 调用修改图书总量类方法
Library.add_books(190)

# 调用还书方法
lib1.return_book(0)
lib2.return_book(70)

# 调用借书方法
lib1.borrowed_book(1)
lib2.borrowed_book(80)



# # 调用get_book_status类方法
# lib1.get_book_status()


