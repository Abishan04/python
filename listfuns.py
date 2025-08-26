subjects = ["maths","tamil","english"]
#subjects[3] = "ict"
subjects.append("ict")
print(subjects)
subjects.insert(2,"science")
print(subjects)
subjects.extend(["history","physics"])
print(subjects)
subjects.pop(2)
print(subjects)
subjects.pop()
print(subjects)#delete final index
subjects.remove("history")
print(subjects)#delete final index
if "tamil" in subjects:
    subjects.remove("tamil")
print(subjects)

#subjects.clear()
subjects.append("ict")
print(subjects)
print(subjects.index("maths"))

subjects.sort(reverse = True)
print(subjects)

marks = [34,6,78,56,90]
print(max(marks))
print(min(marks))
print(sum(marks))

marksF = marks
print(marksF)
print(marks)

marksD = marks.copy()
print(marksD)
marksD[3] = 45
print(marks)