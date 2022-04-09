happiness = 0
arr_len, point_len = map(int, input().split())
arr = list(map(int, input().split()))
good = set(map(int, input().split()))
bad = set(map(int, input().split()))

for i in arr:
    if i in good:
        happiness += 1
    elif i in bad:
        happiness -= 1
print(happiness)
