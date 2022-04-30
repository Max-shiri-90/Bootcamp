from itertools import combinations_with_replacement as cwr


string, number = input().split()

for _ in cwr(sorted(string), int(number)):
    print("".join(_))
