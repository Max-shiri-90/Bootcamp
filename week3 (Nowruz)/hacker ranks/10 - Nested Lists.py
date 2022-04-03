Result = []
score_list = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result += [[name, score]]
        score_list += [score]
    lowest = sorted(list(set(score_list)))[1]
    for x, y in sorted(Result):
        if y == lowest:
            print(x)
