class Fraction:
    def __init__(self, x=0, y=1):
        self.num = x
        self.denom = y

    def gcd(self, a, b):
        r = a % b
        while r != 0:
            a = b
            b = r
            r = a % b
        return b

    def reduce_fraction(self):
        if self.num == 0:
            self.denom = 1
            return

        x = self.gcd(abs(self.num), abs(self.denom))
        self.num = self.num // x
        self.denom = self.denom // x

    def __str__(self):
        s = f"{self.num} {self.denom}"
        return s


N = int(input())
fractions = []

for _ in range(N):
    x, y = map(int, input().split())
    fraction = Fraction(x, y)
    fractions.append(fraction)

largest_fraction = fractions[0]

for fraction in fractions:
    fraction.reduce_fraction()
    if (fraction.num * largest_fraction.denom) > (
        largest_fraction.num * fraction.denom
    ):
        largest_fraction = fraction

print(largest_fraction)
