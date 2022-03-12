def even_numbers(x):
    while x in range(101):
        if x % 2 == 0:
            print(x)
        x += 1


even_numbers(x=1)
