import re

test_cases_len = int(input())
for elm in range(test_cases_len):
    try:
        print(bool(re.compile(input())))
    except:
        print('False')
