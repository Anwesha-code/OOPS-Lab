# Write a python program to check whether a number is strong number or not

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def is_strong_number(num):
    sum_of_factorials = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_factorials += factorial(digit)
        temp //= 10

    if sum_of_factorials == num:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_strong_number(num):
    print(f"{num} is a Strong Number.")
else:
    print(f"{num} is not a Strong Number.")
