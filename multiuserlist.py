# Get subjects from user
subjects = input("Enter subjects separated by commas (e.g. Maths,Physics,Chemistry): ").split(",")
subjects = [s.strip() for s in subjects]  # Clean whitespace

# Get number of students
num_students = int(input("Enter number of students: "))
students = []

# Collect student data
for i in range(num_students):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Name: ")
    marks = []
    for subject in subjects:
        mark = int(input(f"{subject} mark: "))
        marks.append(mark)
    students.append([name] + marks)

# Print header
header = ["Name"] + subjects + ["Total", "Avg", "Result"]
print("\n" + "".join(f"{h:<12}" for h in header))

# Process and print each student's result
for student in students:
    name = student[0]
    marks = student[1:]
    total = sum(marks)
    avg = total / len(marks)

    if avg >= 75:
        result = "A"
    elif avg >= 65:
        result = "B"
    elif avg >= 55:
        result = "C"
    elif avg >= 40:
        result = "S"
    else:
        result = "F"

    row = [name] + marks + [total, f"{avg:.2f}", result]
    print("".join(f"{str(item):<12}" for item in row))