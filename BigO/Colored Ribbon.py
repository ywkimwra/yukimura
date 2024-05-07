class Ribbon:
    def __init__(self, color, length):
        self.color = color
        self.length = length


n = int(input())
ribbons = []

for _ in range(n):
    p, l = map(int, input().split())
    ribbon = Ribbon(p, l)
    ribbons.append(ribbon)

color_stats = []

for ribbon in ribbons:
    color = ribbon.color
    length = ribbon.length
    found = False

    for i in range(len(color_stats)):
        if color_stats[i][0] == color:
            color_stats[i][1] += length
            color_stats[i][2] += 1
            found = True
            break

    if not found:
        color_stats.append([color, length, 1])

x = len(color_stats)

for i in range(x - 1):
    for j in range(x - i - 1):
        if int(color_stats[j][0]) > int(color_stats[j + 1][0]):
            color_stats[j], color_stats[j + 1] = color_stats[j + 1], color_stats[j]

print(len(color_stats))

for color, length, quantity in color_stats:
    print(f"{color} {length} {quantity}")
