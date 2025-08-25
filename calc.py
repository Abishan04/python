students = [
    ["Abi", 90, 85, 88],
    ["Mathi", 75, 80, 70],
    ["Janan", 65, 60, 72],
    ["Habin", 95, 92, 96],
    ["Pran", 82, 78, 80]
]
header = ["Name", "Maths", "Physics", "Chemistry", "Total", "Avg", "Result"]

print(f"{header[0]:<10}{header[1]:>8}{header[2]:>8}{header[3]:>10}{header[4]:>8}{header[5]:>8}{header[6]:>10}")


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

    print(f"{name:<10}{marks[0]:>8}{marks[1]:>8}{marks[2]:>10}{total:>8}{avg:>8.2f}{result:>8}")
