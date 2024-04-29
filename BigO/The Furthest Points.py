import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        s = f"{self.x} {self.y}"
        return s


Mx, My = map(int, input().split())
M = Point(Mx, My)

N = int(input())
points = []

for _ in range(N):
    xi, yi = map(int, input().split())
    point = Point(xi, yi)
    points.append(point)

max_distance = 0
furthest_point = None

for point in points:
    dist = M.distance(point)
    if dist > max_distance:
        max_distance = dist
        furthest_point = point

print(furthest_point)
