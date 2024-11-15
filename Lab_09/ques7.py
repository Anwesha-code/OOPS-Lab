# Implement selection sort using python using classes and methods.

class SelectionSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        n = len(self.data)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.data[j] < self.data[min_index]:
                    min_index = i
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]

    def display(self):
        print("Sorted data:", self.data)

data = [34, 63, 78, 22, 21]
selection_sort = SelectionSort(data)
selection_sort.sort()
selection_sort.display()
