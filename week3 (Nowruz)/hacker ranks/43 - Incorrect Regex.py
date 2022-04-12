import re


test_case = int(input())
for elm in range(test_case):
    try:
        print(bool(re.compile(input())))
    except:
        print('False')
