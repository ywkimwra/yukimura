#logical operators = used on conditional statements

# and = checks two or more conditions if True
#  or = checks if at least one condition is True
# not = True if condition is False, and vice versa

temp = 12
sunny = True

#if temp > 0 and temp < 50:
#    print("The temperature is good")
#else:
#    print("The temperature is bad")

#if temp <= 0 or temp >= 50:
#    print("The temperature is bad")
#else:
#    print("The temperature is good")

if temp > 0 and temp < 50:
    print("The temperature is good")
else:
    print("The temperature is bad")

if not sunny:
    print("It is cloudy outside")
else:
    print("It is sunny outside")