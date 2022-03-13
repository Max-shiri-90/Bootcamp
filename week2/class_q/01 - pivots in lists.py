def pivot(lst):
    result = []
    if lst[0] < lst[1]:
        for i in range(len(lst) - 2):
            if lst[i] < lst[i + 1] and lst[i + 1] > lst[i + 2]:
                result.append(lst[i + 1])
    elif lst[0] > lst[1]:
        for i in range(len(lst) - 2):
            if lst[i] > lst[i + 1] and lst[i + 1] < lst[i + 2]:
                result.append(lst[i + 1])
    print(result)
    print(len(result))


pivot(lst=[1, 2, 3, 8, 9, 21, 12, 15, 18, 42])
pivot(lst=[1, 8, 12, 9, 1, 5, 12, 21, 3, 4, 9, 2, 5])
