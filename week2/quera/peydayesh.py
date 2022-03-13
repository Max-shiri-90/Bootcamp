input_list = []
total_list = [1, 2, 3, 4]
compared_list = []


def find(num1, num2, num3):
    input_list.append(int(num1))
    input_list.append(int(num2))
    input_list.append(int(num3))
    for i in total_list:
        if i not in input_list:
            compared_list.append(i)
    print(compared_list[0])


find(num1=input(), num2=input(), num3=input())

