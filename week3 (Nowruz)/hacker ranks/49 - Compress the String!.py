from itertools import groupby


print(*[(len(list(count)), int(num)) for num, count in groupby(input())])
