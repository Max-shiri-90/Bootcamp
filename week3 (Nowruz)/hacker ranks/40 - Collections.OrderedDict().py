from collections import OrderedDict


order = OrderedDict()
for i in range(int(input())):
    name, space, price = input().rpartition(' ')
    order[name] = order.get(name, 0) + int(price)
for name, price in order.items():
    print(name, price)
