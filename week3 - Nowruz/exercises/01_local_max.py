def local_max(len_list, lst):
    lst = list(map(int, lst.split()))[:len_list]
    changes_counter = 0
    i = 1
    output_lst = [lst[0]]  # first
    for elm in range(len(lst) - 2):
        if lst[elm] < lst[elm + 1] and lst[elm + 1] > lst[elm + 2]:  # local maximum
            output_lst.append(lst[elm + 1])
            i += 1
        elif lst[elm] < lst[elm + 1] < lst[elm + 2]:  # increased row
            output_lst.append(lst[elm + 2])
            changes_counter += 1
        else:
            if i % 2 == 0:
                output_lst.append(max(lst[elm], lst[elm + 2]))
                changes_counter += 1
            else:
                output_lst.append(lst[elm + 1])
    output_lst.append(lst[-1])  # last
    print(changes_counter)
    print(*output_lst)


local_max(len_list=int(input()), lst=input())

# 2 1 2
# 1 2 3 1
# 1 2 1 2 1
# 1 2 1 3 2 3 1 2 1
# 2 1 3 1 3 1 3 1 3
