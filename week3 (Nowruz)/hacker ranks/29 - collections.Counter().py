from collections import Counter


numShoes = int(input())
shoes = Counter(map(int, input().split()))
numCust = int(input())
sale = 0
for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]: 
        sale += price
        shoes[size] -= 1
print(sale)

