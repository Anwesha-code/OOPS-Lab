# Write a program in python to use various inbuilt functions of a list

my_list = [10, 20, 30, 40, 50]

my_list.append(60)
print("After append(60):", my_list)

my_list.insert(2, 25)
print("After insert(2, 25):", my_list)

my_list.extend([70, 80])
print("After extend([70, 80]):", my_list)

my_list.remove(30)
print("After remove(30):", my_list)

popped_element = my_list.pop()
print("After pop():", my_list, "| Popped element:", popped_element)

index_of_40 = my_list.index(40)
print("Index of 40:", index_of_40)

count_of_20 = my_list.count(20)
print("Count of 20:", count_of_20)


