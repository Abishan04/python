students = []
num_of_students = int(input("Enter the number of students: "))

subjects = []
num_of_subjects = int(input("Enter the number of subjects: "))

for i in range(num_of_subjects):
    subject_name = input("Enter subject " + str(i + 1) + " name: ")
    subjects.append(subject_name)

for i in range(num_of_students):
    student_name = input("Enter student " + str(i + 1) + " name: ")
    marks = []
    for j in range(num_of_subjects):
        mark = int(input("Enter mark of " + student_name + " in " + subjects[j] + ": "))
        marks.append(mark)
    students.append([student_name] + marks)

averages = [sum(s[1:]) / len(subjects) for s in students]
original_averages = averages.copy()
sorted_averages = sorted(averages, reverse=True)

header = f"{'Name':<10}"
for subject in subjects:
    header += f"{subject:>8}"
header += f"{'Total':>8}{'Avg':>8}{'Grade':>8}"
print()
print(header)

for avg in sorted_averages:
    index = original_averages.index(avg)
    student = students[index]
    name = student[0]
    marks = student[1:]
    total = sum(marks)

    if avg >= 75:
        grade = "A"
    elif avg >= 65:
        grade = "B"
    elif avg >= 55:
        grade = "C"
    elif avg >= 40:
        grade = "S"
    else:
        grade = "F"

    details = f"{name:<10}"
    for mark in marks:
        details += f"{mark:>8}"
    details += f"{total:>8}{avg:>8.2f}{grade:>8}"
    print(details)

print("\nMaximum marks per subject:")
for i in range(len(subjects)):
    max_mark = max(student[i + 1] for student in students)
    print(f"{subjects[i]:<10}: {max_mark}")

print("\nMinimum marks per subject:")
for i in range(len(subjects)):
    min_mark = min(student[i + 1] for student in students)
    print(f"{subjects[i]:<10}: {min_mark}")