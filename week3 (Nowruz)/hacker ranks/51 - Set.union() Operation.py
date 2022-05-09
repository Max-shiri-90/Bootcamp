first_set_count = input()
first_set = set(map(int, input().split()))

second_set_count = input()
second_set = set(map(int, input().split()))

print(len(first_set.union(second_set)))
