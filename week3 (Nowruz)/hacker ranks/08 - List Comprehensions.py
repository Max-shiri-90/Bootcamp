if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    final_lst = []
    inner_lst = []
    for x in range(x + 1):
        for y in range(y + 1):
            for z in range(z + 1):
                if x + y + z != n:
                    inner_lst = [x, y, z]
                    final_lst.append(inner_lst)
print(final_lst)
