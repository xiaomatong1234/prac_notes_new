class Rectangle:
    @staticmethod
    def num(a,b):
        return a*b
    @staticmethod
    def num2(a, b):
        return (a + b )*2

print(f'矩形的面积为：{Rectangle.num(2,3)}')
print(f'矩形的周长为：{Rectangle.num2(2,3)}')
