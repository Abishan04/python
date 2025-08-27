'''
s = {"maths","tamil","science","tamil"}
print(s)
print(type(s))
s.add("it")
print(s)
s.update(["physics","chemistry","biology"])
print(s)
s.remove('biology')
print(s)
s.discard('chemistry')
print(s)
s.pop()
print(s)
s.clear()
print(s)
numbers = [70,49,50,26,50,49,20]
print(numbers)
number2 = set(numbers)
print(number2)

a = {1,2,3,4,5}
b = {3,5,7,8,9}
c = {}
c = a|b # refers to union
c = a.union(b)
d = a & b # refers to intersection
d = a.intersection(b)
e = a - b# refers to difference
e = a.difference(b)
e = b - a# refers to difference
e = b.difference(a)
f = a ^ b# refers to symmetric difference
f = a.symmetric_difference(b)
print(f)
'''
a = {1,2,3}
b = {1,2,3,4,5}
c = {4,5,6}
d = a|b|c
e = a&b&c
print(d)

print(a<=b)
print(a.issubset(b))
print(b.issuperset(a))

