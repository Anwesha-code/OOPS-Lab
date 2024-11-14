# Write a python program to find the factorial of any number using reduce function

from functools import reduce

num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print(f"The factorial of {num} is 1.")
else:
    factorial = reduce(lambda x, y: x * y, range(1, num + 1))
    print(f"The factorial of {num} is {factorial}.")
