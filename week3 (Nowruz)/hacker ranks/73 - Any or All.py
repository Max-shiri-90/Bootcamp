n = int(input())
integer = input().split(" ")
print(all(int(i)>=0 for i in integer) and any(i == i[::-1]for i in integer))
