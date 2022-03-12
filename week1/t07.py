for x in reversed(range(20, 201)):
    if x % 5 == 0:
        if x % 3 == 0:
            continue
        print(x)
