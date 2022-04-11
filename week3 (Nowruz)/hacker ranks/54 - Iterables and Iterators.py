from itertools import combinations

N = int(input())
letters = list(input().split(" "))
K = int(input())
mojood = 0

joftha = list(combinations(letters, K))
for i in joftha:
    if 'a' in i:
        mojood += 1

print(mojood/len(joftha))
