# Pattern printing
num_rows = 5
for i in range (1, num_rows+1):
    print(''*(num_rows-i-1), end='')
    for j in range(2*i-1):
        print(j, end='')
    print()