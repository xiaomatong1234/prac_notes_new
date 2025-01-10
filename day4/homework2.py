"""
编写一个 Python 程序，输出所有由数字 1、2、3、4 组成的互不相同且无重复数字的三位数。
即个位，十位，百位互不相同且无重复数字。
"""
import itertools
def three_num():
    # 取出个位、十位、百位的数字
    # 判断 个位、十位、百位是否互不相同 去除两两相通、三个都相同的情况
    # 列表形式输出三位数
    result = []
    for a in range(1,5):
        for b in range(1, 5):
            for c in range(1, 5):
            # print(b, end=' ')
                if a != b & b != c & c != a:
                    result.append("%d%d%d" % (a,b,c))
    return result


if __name__ == '__main__':
    print(three_num())

print('-----------------------permutations-------------------------')

def three_perms():

    result = []
    three_digit_nums = itertools.permutations(digits, 3)
    result.append(list(three_digit_nums))
    return result

digits = [1,2,3,4]
if __name__ == '__main__':
    print(three_perms())