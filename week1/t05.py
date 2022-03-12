def my_multiple(x, y):
    m = 1
    z = 0
    while m <= y:
        z += x
        m += 1
    print(z)


my_multiple(x=int(input("Enter a number: ")), y=int(input("Enter another number: ")))
