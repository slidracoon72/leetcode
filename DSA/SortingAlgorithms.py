from collections import defaultdict
from typing import List


class SortingAlgorithms:
    # Quick Sort is a divide-and-conquer algorithm that works by selecting a 'pivot'
    # element from the array and partitioning the other elements into two sub-arrays,
    # according to whether they are less than or greater than the pivot.
    # The sub-arrays are then sorted recursively.
    # Time: O(nlogn), Space: O(logn)
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    # Merge Sort is a divide-and-conquer algorithm that divides the array into two halves,
    # sorts each half, and then merges the sorted halves to produce a sorted array.
    # Time: O(nlogn), Space: O(n)
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # Insertion Sort builds the final sorted array one item at a time.
    # It is much less efficient on large lists than more advanced algorithms
    # such as quicksort, heapsort, or merge sort.
    # Time: O(n^2), Space: O(1)
    # Inplace algorithm
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    # Counting Sort is an integer sorting algorithm that works by counting
    # the number of objects that have each distinct key value, and using arithmetic
    # to determine the positions of each key in the output sequence. It is suitable
    # for sorting elements with a bounded range.
    # Time: O(n+k), Space: O(k); n = no. of elements, k = range of input
    # Inplace algorithm
    def counting_sort(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return arr

        # Initialize the count dictionary
        count = defaultdict(int)

        # Count each element
        for num in arr:
            count[num] += 1

        current_index = 0
        for num in range(min(count), max(count) + 1):
            while count[num] > 0:
                arr[current_index] = num
                current_index += 1
                count[num] -= 1

        return arr

    # Bubble Sort is a simple comparison-based sorting algorithm. It works by
    # repeatedly stepping through the list to be sorted, comparing adjacent elements,
    # and swapping them if they are in the wrong order. The pass through the list is
    # repeated until the list is sorted.
    # Time: o(n^2), Space: O(1)
    # Inplace algorithm
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

    # Selection Sort is an in-place comparison-based algorithm. It works by
    # dividing the input list into two parts: the sublist of items already sorted,
    # which is built up from left to right, and the sublist of items remaining to be sorted.
    # Initially, the sorted sublist is empty and the unsorted sublist is the entire input list.
    # The algorithm proceeds by finding the smallest (or largest, depending on the sorting order)
    # element in the unsorted sublist, swapping it with the leftmost unsorted element, and moving
    # the sublist boundaries one element to the right
    # Time: o(n^2), Space: O(1)
    # Inplace algorithm
    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    # Heap Sort is a comparison-based sorting technique based on a binary heap data structure.
    # It is similar to selection sort where we first find the maximum element and place it at the end.
    # We repeat the same process for the remaining elements.
    # Time: o(nlogn), Space: O(1)
    # Inplace algorithm
    def heapify(self, arr, n, i):
        """
        Ensure the subtree rooted at index i is a max heap.
        :param arr: List of elements to be sorted
        :param n: Size of the heap
        :param i: Index of the root element of the subtree
        """
        largest = i  # Initialize largest as root
        left = 2 * i + 1  # Left child index
        right = 2 * i + 2  # Right child index

        # If the left child is larger than the root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # If the right child is larger than the largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If the largest is not the root, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            self.heapify(arr, n, largest)  # Recursively heapify the affected subtree

    def heap_sort(self, arr):
        """
        Perform heap sort on the given list.
        :param arr: List of elements to be sorted
        """
        n = len(arr)

        # Build a max heap (rearrange the array)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # One by one extract elements from the heap
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Swap the current root (maximum) to the end
            self.heapify(arr, i, 0)  # Call max heapify on the reduced heap

        return arr


c = SortingAlgorithms()
arr = [5, 9, 2, 4, -3, 8, 90, 5, 6, 1]
print(arr)
# print(c.quick_sort(arr))
# print(c.merge_sort(arr))
# print(c.insertion_sort(arr))
# print(c.counting_sort(arr))
# print(c.bubble_sort(arr))
# print(c.selection_sort(arr))
print(c.heap_sort(arr))
