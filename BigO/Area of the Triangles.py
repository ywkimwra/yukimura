import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


n = int(input())
total_area = 0

for _ in range(n):
    points = []
    for _ in range(3):
        xi, yi = map(int, input().split())
        point = Point(xi, yi)
        points.append(point)

    a = points[0].distance(points[1])
    b = points[1].distance(points[2])
    c = points[2].distance(points[0])

    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    total_area += area

print(f"{total_area:.2f}")
