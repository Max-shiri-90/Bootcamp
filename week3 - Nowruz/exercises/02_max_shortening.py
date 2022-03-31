def max_shortening(decimal_num):
    i = 0
    lst = []
    while i < len(decimal_num) - 1:
        sum_num = int(decimal_num[i]) + int(decimal_num[i + 1])
        remove_digit = decimal_num.replace(decimal_num[i], '', 1)
        final = remove_digit.replace(remove_digit[i], str(sum_num), 1)
        lst.append(final)

        i += 1
    print(max(lst))


max_shortening(decimal_num=input())

# 10038
