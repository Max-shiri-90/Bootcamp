def hanoi_tower(disk, source_pole, middle_pole, destination_pole):
    if disk == 1:
        print("Move disc 1 from pole", source_pole, "to pole", destination_pole)
        return
    hanoi_tower(disk - 1, source_pole, middle_pole, destination_pole)
    print("Move disc", disk, "from pole", source_pole, "to pole", destination_pole)
    hanoi_tower(disk - 1, middle_pole, destination_pole, source_pole)


disk_num = 3
hanoi_tower(disk_num, 'A', 'C', 'B')
