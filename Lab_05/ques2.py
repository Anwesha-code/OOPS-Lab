# Write a python program to find the largest among three numbers using reduce function

from functools import reduce

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
numbers = [num1, num2, num3]
largest = reduce(lambda x, y: x if x > y else y, numbers)
print("The largest number is:", largest)
