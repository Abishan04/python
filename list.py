'''
print(subjects)
print(subjects[0])
print(subjects[-1])
print(len(subjects))

x = 0
while x < len(subjects):
    print(subjects[x])
    x+=1

print(type(subjects))
subjects[0] = "mathematics"
print(subjects[0])
'''
subjects = ["Maths","Tamil","Science","English","Ict"]
print(subjects[3:5])#3 is index 5 is element
print(subjects[:3])#these are element
print(subjects[2:])#these are element
print(subjects[::3])#it go increase by 3
