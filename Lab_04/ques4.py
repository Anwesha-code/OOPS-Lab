# Pattern Printing

num_rows = 5
for i in range(num_rows):
    character = chr(65+i)
    for j in range(i+1):
        print(character, end= '')
    print()