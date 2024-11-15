# Implement insertion sort in python using classes and methods

class InsertionSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >= 0 and key < self.data[j]:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key

    def display(self):
        print("Sorted data:", self.data)

data = [13, 14, 10, 4, 8]
insertion_sort = InsertionSort(data)
insertion_sort.sort()
insertion_sort.display()


