#!usr/bin/python3
import random
number = random.randint(-1000, 1000)
dig = abs(number % 10)

if dig > 5:
    print(f"last digit of {number} is {dig} and is greater than 5")
elif dig == 0:
    print(f"last digit of {number} is {dig} and is 0")
else dig !=0 and dig < 6:
    print(f"last digit of {number} is {dig} and is less than 6 and not 0")
