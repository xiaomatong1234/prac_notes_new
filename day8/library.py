"""
1. 图书类 Book：属性包括书名（title）、作者（author）和出版日期（publish_date），方法包括获取书名、获取作者和获取出版日期的方法。
2. 图书馆类 Library：属性包括图书列表（books），方法包括添加图书、借出图书、归还图书和显示所有图书的方法。

3. add_book 方法：接受一个 Book 类型的参数，将其添加到图书列表中。
4. borrow_book 方法：接受一个字符串类型的参数（书名），找到对应书名的图书，并将其从图书列表中移除。
5. return_book 方法：接受一个 Book 类型的参数，将其添加到图书列表中。
6. show_books 方法：输出当前图书馆中所有图书的书名、作者和出版日期。
"""
class Book:
    """创建一个图书类"""
    def __init__(self,title,author,publish_date):
        """
        初始化图书的实例属性
        :param title: 书名
        :param author: 作者
        :param publish_date: 出版日期
        """
        self.title = title
        self.author = author
        self.publish_date = publish_date
    def get_title(self):
        """获取书名"""
        return self.title
    def get_author(self):
        """获取作者"""
        return self.author
    def get_publish_date(self):
        """获取出版日期"""
        return self.publish_date

class Library:
    """创建一个图书馆类"""
    def __init__(self):
        """初始化图书馆属性"""
        self.book_lst = [] # 定义一个图书馆列表

    def add_book(self,book):
        """添加图书"""
        # 判断添加的书是否在图书列表
        if book not in self.book_lst:
            self.book_lst.append(book)
            print(f'添加图书：《{book.get_title()}》成功！')
        else:
            print(f'图书：《{book.get_title()}》已存在，添加失败！！！')

    def borrow_book(self,book_name):
        """借出图书"""
        # 遍历图书列表
        for book in self.book_lst:
            # 判断借出的书是否在图书列表
            if book.title == book_name:
                self.book_lst.remove(book)
                print(f'\n图书：《{book.get_title()}》成功从图书列表借出！')
            else:
                print(f'图书：《{book_name}》不存在，借出失败！！！')

    def return_book(self,book):
        """归还图书"""
        # 判断归还的图书是否在图书列表
        if book not in self.book_lst:
            self.book_lst.append(book)
            print(f'\n图书：《{book.get_title()}》归还成功！')
        else:
            print(f'图书：《{book.get_title()}》在图书列表存在，归还失败！！！')

    def show_book(self):
        """展示图书"""
        for book in self.book_lst:
            book_info = f'\n书名：《{book.get_title()}》，作者：{book.get_author()}，出版日期：{book.get_publish_date()}'
            print('\n图书馆中现有的书籍',book_info)

# 实例化 图书对象
book1 = Book('Python入门教程','张三','2020-01-01')
book2 = Book('Java入门教程','李四','2020-02-01')

# 实例化 图书馆对象
library = Library()
# 添加图书
library.add_book(book1)
library.add_book(book2)
# 展示图书
library.show_book()
# 借出图书
library.borrow_book('Python入门教程')
library.borrow_book('A入门教程1')
# 归还图书
library.return_book(book1)
library.return_book(book1)
# 展示图书
library.show_book()