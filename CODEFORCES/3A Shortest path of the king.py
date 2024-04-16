#https://codeforces.com/problemset/problem/3/A

location = input().lower()
destination = input().lower()
move_counter = 0
move = []
h1 a8

while location != destination:
    if (location[0] < destination[0]) and (location[1] < destination[1]):
        move_counter += 1
        move.append("RU")
        # update location
    
    if (location[0] < destination[0]) and (location[1] > destination[1]):
        move_counter += 1
        move.append("RD")
        # update location
    
    if (location[0] > destination[0]) and (location[1] < destination[1]):
        move_counter += 1
        move.append("LU")
        #update location
    
    if (location[0] > destination[0]) and (location[1] > destination[1]):
        move_counter += 1
        move.append("LD")
        #update location
    
    if lo
