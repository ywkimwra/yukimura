class Student:
    def __init__(self, id, math, literature):
        self.id = id
        self.math = math
        self.literature = literature


n, q = map(int, input().split())
students = []

for _ in range(n):
    id, math, literature = map(str, input().split())
    student = Student(id, math, literature)
    students.append(student)

for _ in range(q):
    query_id = input()
    for student in students:
        if student.id == query_id:
            print(f"{student.math} {student.literature}")
            break