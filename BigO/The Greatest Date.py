class Date:
    def __init__(self, a, b, c):
        self.day = a
        self.month = b
        self.year = c

    def __str__(self):
        s = f"{self.day} {self.month} {self.year}"
        return s


N = int(input())
dates = []

for i in range(N):
    a, b, c = map(int, input().split())
    date = Date(a, b, c)
    dates.append(date)

greatest_date = dates[0]

for i in range(1, len(dates)):
    if dates[i].year > greatest_date.year:
        greatest_date = dates[i]
    elif dates[i].year == greatest_date.year and dates[i].month > greatest_date.month:
        greatest_date = dates[i]
    elif (
        dates[i].year == greatest_date.year
        and dates[i].month == greatest_date.month
        and dates[i].day > greatest_date.day
    ):
        greatest_date = dates[i]

print(greatest_date)
