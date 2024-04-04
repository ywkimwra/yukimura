"""
fruits =        ["grape", "orange", "apple", "pineapple", "avocado"]
vegetables =    ["carrots", "tomatoes", "potatoes", "broccoli", "cucumbers"]
meats =         ["chicken", "fish", "beef", "pork", "turkey"]

groceries = [fruits, vegetables, meats]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
"""

row1 = [7, 8, 9]
row2 = [4 ,5 ,6]
row3 = [1, 2, 3]
row4 = ["*", 0, "#"]

numpad = [row1, row2, row3, row4]

for rows in numpad:
    for num in rows:
        print(num, end=" ")
    print()