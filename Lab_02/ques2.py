# Write a python to calculate factorials of number from 1 to 50 and print them

factorial = 1

for i in range(1, 51):
    factorial *= i  
    print(f"Factorial of {i} is {factorial}")
