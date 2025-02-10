filenames = ['cat.txt', 'dog.txt', 'li.txt']
for filename in filenames:
    print(f'\nReading file:{filename}')
    try:
        with open(filename,'r') as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print('File not found')



