from collections import defaultdict


dif_l = defaultdict(list)
n, m = map(int, input().split())
for i in range(n):
    dif_l[input()].append(str(i + 1))
for j in range(m):
    print(' '.join(dif_l[input()]) or -1)

