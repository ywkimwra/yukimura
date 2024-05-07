grades = []

while True:
    n = float(input())
    if n == -1:
        break
    else:
        grades.append(n)

for grade in grades:
    if grade < 5:
        print(grade)
