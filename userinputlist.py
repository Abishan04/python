def get_subjects():
    sub_count = int(input("Enter number of subjects: "))
    return [input(f"Enter name of subject {i+1}: ") for i in range(sub_count)]

def get_student_data(subjects, stu_count):
    students = []
    for i in range(stu_count):
        name = input(f"\nEnter name of student {i+1}: ")
        marks = [int(input(f"Enter marks for {subject}: ")) for subject in subjects]
        students.append({'name': name, 'marks': marks})
    return students

def calculate_grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 55:
        return "C"
    elif avg >= 40:
        return "S"
    else:
        return "F"

def print_report(subjects, students):
    header = f"{'Name':<10}" + ''.join(f"{sub:>8}" for sub in subjects)
    header += f"{'Total':>8}{'Avg':>8}{'Grade':>8}"
    print("\n" + header)

    for student in students:
        name = student['name']
        marks = student['marks']
        total = sum(marks)
        avg = total / len(marks)
        grade = calculate_grade(avg)
        row = f"{name:<10}" + ''.join(f"{mark:>8}" for mark in marks)
        row += f"{total:>8}{avg:>8.2f}{grade:>8}"
        print(row)

# Main execution
stu_count = int(input("Enter number of students: "))
subjects = get_subjects()
students = get_student_data(subjects, stu_count)
print_report(subjects, students)