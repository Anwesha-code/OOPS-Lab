#write a pthon code to check whether a number is armstron number or not

num = int(input("Enter a number: "))
num_digits = len(str(num))

sum_of_powers = 0

sum_of_powers = sum(int(digit) ** num_digits for digit in str(num))

if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
