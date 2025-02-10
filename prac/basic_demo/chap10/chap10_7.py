"""练习10-7：加法计算器　
将为完成练习10-6而编写的代码放在一个while循环中，
让用户犯错（输入的是文本而不是数）后能够继续输入数。
"""
while True:
    try:
        num1 = input('Enter a first number: ')
        if num1 == "q":
            break
        num1 = float(num1)

        num2 = input('Enter a second number: ')
        if num2 == "q":
            break
        num2 = float(num2)

    except ValueError:
        print('Invalid input')
    else:
        result = num1 + num2
        print(num1,'+', num2, '=', result)

