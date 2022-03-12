def max_min_finder(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        maximum = num1
        minimum = min(num2, num3)
    elif (num2 >= num1) and (num2 >= num3):
        maximum = num2
        minimum = min(num1, num3)
    else:
        maximum = num3
        minimum = min(num1, num2)

    print("max is: ", maximum)
    print("min is: ", minimum)


max_min_finder(num1=float(input("Enter the first number: ")),
               num2=float(input("Enter the second number: ")),
               num3=float(input("Enter the third number: ")))
