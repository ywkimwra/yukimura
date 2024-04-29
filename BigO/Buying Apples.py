class Apple:
    def __init__(self, a, b):
        self.weight = a
        self.price = b


n = int(input())
apples = []

for _ in range(n):
    w, p = map(int, input().split())
    apple = Apple(w, p)
    apples.append(apple)

best_apple = apples[0]
index = 0
for i in range(len(apples)):
    if (apples[i].weight > best_apple.weight) or (
        (apples[i].weight == best_apple.weight) and (apples[i].price > best_apple.price)
    ):
        best_apple = apples[i]
        index = i

print(index)
