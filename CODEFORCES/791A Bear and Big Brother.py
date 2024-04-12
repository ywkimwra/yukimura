#https://codeforces.com/problemset/problem/791/A

a, b = map(int, input().split())
year_counter = 0
while a <= b:
    a *= 3
    b *= 2
    year_counter += 1

print(year_counter)