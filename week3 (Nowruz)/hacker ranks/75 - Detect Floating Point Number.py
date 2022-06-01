import re
for _ in range(int(input())):
    x = re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())
    print(bool(x))

