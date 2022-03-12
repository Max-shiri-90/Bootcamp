def odd_even_detector(number):
    if (number % 2) == 0:
        print("{0} is Even".format(number))
    else:
        print("{0} is Odd".format(number))


odd_even_detector(number=int(input("Enter a number: ")))
