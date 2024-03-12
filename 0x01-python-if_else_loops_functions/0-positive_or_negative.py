#!usr/bin/python3
import random
number = random.randint(-100, 100)
print("The number", number, end="")
if number > 0:
    print("is postive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
