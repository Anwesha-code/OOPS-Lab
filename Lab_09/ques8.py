# Implement merge sort using python using classes and methods

class MergeSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        self.data = self.merge_sort(self.data)

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        left_half = self.merge_sort(left_half)
        right_half = self.merge_sort(right_half)
        return self.merge(left_half, right_half)

    def merge(self, left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged

    def display(self):
        print("Sorted data:", self.data)

data = [38, 27, 43, 3, 9, 82, 10]
merge_sort = MergeSort(data)
merge_sort.sort()
merge_sort.display()