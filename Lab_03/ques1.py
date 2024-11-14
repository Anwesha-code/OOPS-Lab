print("Choose Operation:")
print("1 - Addition ; 2 - Subtraction ; 3 - Multiplication ; 4 - Division")

choice = int(input("Enter your choice of operator (1, 2, 3, 4):"))

op1 = int(input("Enter first operand:"))
op2 = int(input("Enter second operand:"))

if choice == 1:
    result = op1 + op2

elif choice == 2:
    result = op1 - op2

elif choice == 3:
    result = op1 * op2

elif choice == 4:
    result = op1 // op2

else:
    print("Enter a valid choice")

print("Result of the operation is:", result)