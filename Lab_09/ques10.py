# Implement binary search in python using classes and methods

class BinarySearch:
    def __init__(self, data):
        self.data = sorted(data)

    def search(self, target):
        low = 0
        high = len(self.data) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.data[mid] == target:
                return mid
            elif self.data[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1 

    def display(self):
        print("Sorted Data:", self.data)

data = [50, 30, 70, 10, 40, 60, 20]
binary_search = BinarySearch(data)
binary_search.display()  

target = 40
result = binary_search.search(target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
