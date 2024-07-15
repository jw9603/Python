students = [i for i in range(1,31)]

for _ in range(28):
    submit = int(input())
    students.remove(submit)
print(students[0],students[1],sep='\n')