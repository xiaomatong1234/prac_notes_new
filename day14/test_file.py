from pathlib import Path


def test_file():
    files = open('sort.py')
    r = files.read()
    print(r)

    file2 = open('demo.txt')
    files.write('123\n456')
    with open("demo2.txt", 'a+') as files:
        files.write(r)

    # 引入第三方库
    r = Path('demo.txt').read_text(encoding='utf-8')
    Path('demo.txt').write_text('123')










