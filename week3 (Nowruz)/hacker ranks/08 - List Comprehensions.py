if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
all_list = []
for x in range(x + 1):
    for y in range(y + 1):
        for z in range(z + 1):
            all_list.append([x, y, z])
lst = [elm for elm in all_list if sum(elm) != n]
print(lst)
