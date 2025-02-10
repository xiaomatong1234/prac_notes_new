filenames = ['cat.txt', 'dog.txt', 'li.txt']
for filename in filenames:
    try:
        with open(filename,'r') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f'\nReading file:{filename}')
        print(contents)



