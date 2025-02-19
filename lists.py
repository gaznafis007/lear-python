names=["gazi", "nafis", "md", "abdullah"]

print(len(names))
print(names[-3])
print(names[3])

# list methods
names.append("rafi")
print(names)
names.reverse()
names.insert(1, 'gazi')
print(names)
names.clear()
print(names)

marks = [10, 20, 30, 40]
print(marks)
marks.append(50)
print(marks)
marks.reverse()
print(marks)
print(marks.count(0))
marks.insert(0, 60)
print(marks)
print(marks.index(40))
marks.pop(0)
print(marks)
marks.sort()
print(marks)
marks.clear()
print(marks)