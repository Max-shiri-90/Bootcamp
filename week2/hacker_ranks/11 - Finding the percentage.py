if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

the_student = list(student_marks[query_name])
average = sum(the_student) / len(the_student)
print("%.2f" % average)
