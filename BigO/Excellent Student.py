class Student:
    def __init__(self, math=0, writing=0):
        self.math = math
        self.writing = writing

    def gpa(self):
        return (self.math + self.writing) / 2


N = int(input())
count = 0

for _ in range(N):
    S = input()
    a, b = map(float, input().split())

    student = Student(a, b)
    if student.gpa() >= 9.0:
        count += 1

print(count)
