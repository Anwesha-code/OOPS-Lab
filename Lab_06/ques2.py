# Write a python program to pass the list as an argument in a function

def display_list(elements):
    for element in elements:
        print(element, end=" ")
    print()  

def sum_list(elements):
    return sum(elements)


my_list = [10, 20, 30, 40, 50]

print("Original list:")
display_list(my_list)
total = sum_list(my_list)
print("Sum of elements:", total)


