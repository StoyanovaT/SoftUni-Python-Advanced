number_of_students = int(input())
students_info = {}

for _ in range(number_of_students):
    student, grade_as_str = input().split()
    grade = float(grade_as_str)
    if student not in students_info:
        students_info[student] = []

    students_info[student].append(grade)

for key, value in students_info.items():
    print(f"{key} -> {' '.join([f'{el:.2f}' for el in value])} (avg: {(sum(value)/len(value)):.2f})")

