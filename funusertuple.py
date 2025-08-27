def get_input():
    subjects = []
    students = []

    num_of_students = int(input("Enter the number of students: "))
    num_of_subjects = int(input("Enter the number of subjects: "))

    for i in range(num_of_subjects):
        subject_name = input(f"Enter subject {i + 1} name: ")
        subjects.append(subject_name)

    for i in range(num_of_students):
        student_name = input(f"\nEnter student {i + 1} name: ")
        marks = []
        for j in range(num_of_subjects):
            mark = int(input(f"Enter mark of {student_name} in {subjects[j]}: "))
            marks.append(mark)
        students.append([student_name] + marks)

    return subjects, students


def process_results(subjects, students):
    results = []
    averages = [sum(s[1:]) / len(subjects) for s in students]
    original_averages = averages.copy()
    sorted_averages = sorted(averages, reverse=True)

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

        results.append((name, marks, total, avg, grade))

    return results


def print_report(subjects, results, students):
    header = f"{'Name':<10}" + ''.join(f"{subj:>8}" for subj in subjects)
    header += f"{'Total':>8}{'Avg':>8}{'Grade':>8}"
    print("\n" + header)

    for name, marks, total, avg, grade in results:
        row = f"{name:<10}" + ''.join(f"{mark:>8}" for mark in marks)
        row += f"{total:>8}{avg:>8.2f}{grade:>8}"
        print(row)

    print("\nMaximum marks per subject:")
    for i in range(len(subjects)):
        max_mark = max(student[i + 1] for student in students)
        print(f"{subjects[i]:<10}: {max_mark}")

    print("\nMinimum marks per subject:")
    for i in range(len(subjects)):
        min_mark = min(student[i + 1] for student in students)
        print(f"{subjects[i]:<10}: {min_mark}")

subjects, students = get_input()
results = process_results(subjects, students)
print_report(subjects, results, students)