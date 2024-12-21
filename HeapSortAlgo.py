# Heapify function
# Part (a) - Algorithms for Heapsort
# Here are the required algorithms for Heapsort:
# 1. Heapify Algorithm
def heapify(lst, n, i):
    largest = i  # largest as root
    left = 2 * i + 1 
    right = 2 * i + 2

    if left < n and lst[left] > lst[largest]:
        largest = left

    if right < n and lst[right] > lst[largest]:
        largest = right

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)
        heapify(lst, n, largest)  # Recursively heapify the affected subtree

#2. Function to build a max heap
def build_max_heap(lst):
    n = len(lst)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)

#2. Heap sort algorithm
def heapsort(lst):
    n = len(lst)

    build_max_heap(lst)

    for i in range(n - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, i, 0)

# Example usage:
lst = [4, 10, 3, 5, 1]
print("Original list:", lst)
heapsort(lst)
print("Sorted list:", lst)

# Time Complexity
# Heapify: O(log n)
# Build Max Heap: O(n)
# Heapsort: O(n log n)
# Space Complexity
# Heapify: O(1)
# Build Max Heap: O(1)
# Heapsort: O(1)