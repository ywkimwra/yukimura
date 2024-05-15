import sys

sys.setrecursionlimit(1000000000)


class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade


class Node:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None


def insert(root, student):
    if root is None:
        return Node(student)
    if student.grade < root.student.grade:
        root.left = insert(root.left, student)
    elif student.grade > root.student.grade:
        root.right = insert(root.right, student)
    return root


def find_highest_score(root):
    if root is None:
        return None
    if root.right is None:
        return root.student
    return find_highest_score(root.right)


n = int(input())
students = []
for _ in range(n):
    student_id, name, grade = input().split()
    student = Student(student_id, name, float(grade))
    students.append(student)

bst_root = None
for student in students:
    bst_root = insert(bst_root, student)

highest_score_student = find_highest_score(bst_root)

print(
    highest_score_student.student_id,
    highest_score_student.name,
    highest_score_student.grade,
)
