# Implement linear search in python using classes and methods

class LinearSearch:
    def __init__(self, data):
        self.data = data

    def search(self, target):
        for index, value in enumerate(self.data):
            if value == target:
                return index 
        return -1  
    def display(self):
        print("Data:", self.data)

data = [10, 20, 30, 40, 50, 60, 70]
linear_search = LinearSearch(data)
linear_search.display()  
target = 40
result = linear_search.search(target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
