def parallelogram(length, height):
    shape = ' ' * (height - 1) + '*' * length + '\n'
    for i in range(height - 2, 0, -1):
        shape += ' ' * i + '*' + ' ' * (length - 2) + '*\n'
    shape += '*' * length
    print(shape)


parallelogram(length=int(input("Length: ")), height=int(input("Height: ")))
