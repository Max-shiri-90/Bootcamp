A = set(input().split())

for i in range(int(input())):
    if not A.issuperset(set(input().split())):
        print(False)
        break
else:
    print(True)
