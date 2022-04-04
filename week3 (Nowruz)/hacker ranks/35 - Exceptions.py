range_nums = int(input())
for i in range(range_nums):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)
