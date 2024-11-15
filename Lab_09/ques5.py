# Implement bubble sort in python using classes and methods

class BubbleSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

    def display(self):
        print("Sorted data:", self.data)

data = [82, 56, 25, 21, 78, 51, 89]
bubble_sort = BubbleSort(data)
bubble_sort.sort()
bubble_sort.display()

