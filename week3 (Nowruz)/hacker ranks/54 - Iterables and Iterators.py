from itertools import combinations


N = int(input())
letters = list(input().split(" "))
K = int(input())
joftha = list(combinations(letters, K))
mojood = 0

for i in joftha:
    if 'a' in i:
        mojood += 1

print(mojood/len(joftha))
