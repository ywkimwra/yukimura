class Employee:
    def __init__(self, id, name, year):
        self.id = id
        self.name = name
        self.year = year

    def __str__(self):
        s = f"{self.id} {self.name} {self.year}"
        return s


N = int(input())
employees = []

for _ in range(N):
    id, name, year = map(str, input().split())
    employee = Employee(id, name, year)
    employees.append(employee)

oldest_employee = employees[0]

for employee in employees:
    if (int(employee.year) < int(oldest_employee.year)) or (
        (int(employee.year) == int(oldest_employee.year)) and (int(employee.id) < int(oldest_employee.id))
    ):
        oldest_employee = employee

print(oldest_employee)
