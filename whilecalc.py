students = [
    ["Abi", 90, 85, 88],
    ["Mathi", 75, 80, 70],
    ["Janan", 65, 60, 72],
    ["Habin", 95, 92, 96],
    ["Pran", 82, 78, 80]
]
subjects = ["Maths", "Physics", "Chemistry",]
print(f"{'Name':<10}{subjects[0]:>8}{subjects[1]:>8}{subjects[2]:>10}{'Total':>8}{'Avg':>8}{'Result':>8}")

i = 0
while i < len(students):
    name = students[i][0]
    marks = students[i][1:]
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

    print(f"{name:<10}{marks[0]:>8}{marks[1]:>8}{marks[2]:>10}{total:>8}{avg:>8.2f}{result:>8}")
    i += 1