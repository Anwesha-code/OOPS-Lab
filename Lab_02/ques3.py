# Write a python program to calculate sum of elemants of Fibonacci serirs upto n elements

n = int(input("Enter the number of elements: "))

a, b = 0, 1
sum_of_series = 0

for i in range(n):
    sum_of_series += a
    a, b = b, a + b

print(f"The sum of the first {n} elements of the Fibonacci series is:", sum_of_series)
