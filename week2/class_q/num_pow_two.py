def num_pow_two(n):
    k = []
    while n > 0:
        a = int(float(n % 2))
        k.append(a)
        n = (n - a) / 2
    k.append(0)
    string = ""
    for j in k[::-1]:
        string = string + str(j)
    print(string)


num_pow_two(n=int(input()))
