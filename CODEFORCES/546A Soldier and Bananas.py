#https://codeforces.com/problemset/problem/546/A

retail, balance, wants = map(int, input().split())
loan = 0
total = 0

for i in range(1, wants + 1):
    total += (retail * i)
    
loan = total - balance
if loan <= 0:
    print("0")
else:
    print(loan)