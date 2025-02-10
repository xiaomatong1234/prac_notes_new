def display_simulation():
    name = "Twiggy"
    leaves = 0
    for day in range(3):
        leaves += 1
        if leaves == 3:
            print(name, 'is a seedling!')
    print("Leaves:", leaves)


display_simulation()