def concat(path1, path2,path3):
    """
    合并path1, path2,path3
    :param path1:
    :param path2:
    :param path3:
    :return:
    """
    # file_1 = open(path1).read()

    with open(path1) as file:
        content_1 = file.read()
    with open(path2) as file:
        content_2 = file.read()
    add_file = content_1 + content_2

    with open(path3,'w') as file:
        content_3 = file.write(add_file)

    with open(path3) as file:
        final_file = file.read()
        print(final_file)

concat("file1.txt", "file2.txt", "file3.txt")