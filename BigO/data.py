class Fraction:
    # def __init__(self, a = 0, b = 1):
    #     self.num = a
    #     self.denom = b
    
    def set(self, a, b):
        self.num = a
        self.denom = b

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

    def sum_fraction(self, p2):
        p3 = Fraction()
        p3.num = self.num * p2.denom + self.denom * p2.num
        p3.denom = self.denom * p2.denom
        p3.reduce_fraction()
        return p3        

    def __str__(self):
        s = f"{self.num} {self.denom}"
        return s

# x, y = map(int, input().split())
# p1 = Fraction(x, y)

# x, y = map(int, input().split())
# p2 = Fraction(x, y)

# p3 = p1.sum_fraction(p2)

p4 = Fraction()

# print(p3)

p4.set(3, 4)

print(p4)