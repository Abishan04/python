x = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]
for row in x:
    for item in row:
        print(item, end=" ")
    print()

i = 0
while i < 3:
    j = 0
    while j < 3:
        print(x[i][j],end = '')
        j+=1
    i+=1

# 5 students in 1 school
# have 3 subjects in all
# output
# student name maths physics chemsi total avg result

# results a,b,c
# datas nested array