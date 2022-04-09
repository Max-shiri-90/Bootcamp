K = input()
Room_list = input().split()
Room_set = set(Room_list)

for ele in list(Room_set):
    Room_list.remove(ele)
Captain_room = Room_set.difference(set(Room_list)).pop()

print(Captain_room)

# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
