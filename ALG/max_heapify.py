def max_heapify(arr, k, heap_size):
    left_child = 2 * k + 1
    right_child = 2 * k + 2

    # Find the largest among the root, left child, and right child
    largest = k

    # Check if left child exists and is greater than the current largest
    if left_child < heap_size and arr[left_child] is not None and arr[left_child] > arr[largest]:
        largest = left_child

    # Check if right child exists and is greater than the current largest
    if right_child < heap_size and arr[right_child] is not None and arr[right_child] > arr[largest]:
        largest = right_child

    # Swap if the largest is not the root
    if largest != k:
        arr[k], arr[largest] = arr[largest], arr[k]

        # Print intermediate arrays after each step
        print("   Updated A:", A)

        # Recursively heapify the affected subtree
        max_heapify(arr, largest, heap_size)


# Given array A
A = [3, 14, 27, 31, 39, 42, 55, 70, 74, 81, 85, 93, 98]
print("Initially, A:", A)
# Starting from the last non-leaf node and moving upwards
for i in range(len(A) // 2 - 1, -1, -1):
    max_heapify(A, i, len(A))

# The final max-heap
print("Final Max-Heap:", A)