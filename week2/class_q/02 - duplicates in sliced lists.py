from itertools import islice


def pivot1(lst):
    pivot_list = []
    if lst[0] < lst[1]:
        for i in range(len(lst) - 2):
            if lst[i] < lst[i + 1] and lst[i + 1] > lst[i + 2]:
                pivot_list.append(i + 1)
    elif lst[0] > lst[1]:
        for i in range(len(lst) - 2):
            if lst[i] > lst[i + 1] and lst[i + 1] < lst[i + 2]:
                pivot_list.append(i + 1)
    len_list = [pivot_list[0] + 1, pivot_list[1] - pivot_list[0], len(lst) - pivot_list[1] - 1]
    x = iter(lst)
    pivot1.sliced_list1 = [list(islice(x, elem)) for elem in len_list]
    print(pivot1.sliced_list1)


pivot1(lst=[1, 3, 8, 12, 24, 2, 15, 16, 21, 3, 4, 67])


def pivot2(lst):
    pivot_list = []
    if lst[0] < lst[1]:
        for i in range(len(lst) - 2):
            if lst[i] < lst[i + 1] and lst[i + 1] > lst[i + 2]:
                pivot_list.append(i + 1)
    elif lst[0] > lst[1]:
        for i in range(len(lst) - 2):
            if lst[i] > lst[i + 1] and lst[i + 1] < lst[i + 2]:
                pivot_list.append(i + 1)
    len_list = [pivot_list[0] + 1, pivot_list[1] - pivot_list[0], len(lst) - pivot_list[1] - 1]
    x = iter(lst)
    pivot2.sliced_list2 = [list(islice(x, elem)) for elem in len_list]
    print(pivot2.sliced_list2)


pivot2(lst=[1, 8, 9, 21, 2, 16, 17, 7, 28, 67])

result = []


def duplicated_nums(list_a, list_b):
    for k in range(len(list_a)):
        y = [x for x in list_a[k] if x in list_b[k]]
        result.append(y)

    print("\n", result)


duplicated_nums(list_a=pivot1.sliced_list1, list_b=pivot2.sliced_list2)
