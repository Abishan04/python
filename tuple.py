'''
 marks = [23,86,56]
 t = tuple(marks)
 print(t)
 print(type(t))
 print(t.index(23))
marks1 = (23,45,56)
marks2 = (78,59,60)
marks3 = marks1 + marks2
print(marks3)

#unpacking
student = ("Abishan",20,"04/07/2005")
fname,age = student
print(fname)
print(age)
print(dob)
'''
marks = (70,90,58,29,50)
for a,b,c,d,e in marks:
    print(a,b,c,d,e)

