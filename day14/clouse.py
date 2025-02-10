def out_func():
    out_n = 100
    def inner_func():
        print(out_n)
    return inner_func


if __name__ == '__main__':
    of1 = out_func()
    of2 = out_func()

    of1()
    of2()
