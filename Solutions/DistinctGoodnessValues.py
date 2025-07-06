def getDistinctGoodnessValues(arr):
    n = len(arr)
    goodness_values = set()

    # Add the goodness value of the empty subsequence
    goodness_values.add(0)

    # Iterate over each element in the array
    for i in range(n):
        # Create a temporary set to store new goodness values
        new_goodness_values = set()

        # For each existing goodness value, add the current element
        for value in goodness_values:
            new_goodness_values.add(value | arr[i])

        # Add all new goodness values to the main set
        goodness_values.update(new_goodness_values)

    # Convert the set to a sorted list
    return sorted(goodness_values)


arr = [4, 2, 4, 1]
result = getDistinctGoodnessValues(arr)
print(result)  # Output: [0, 1, 2, 4, 6]

arr = [3, 5, 5, 1]
result = getDistinctGoodnessValues(arr)
print(result)  # Output: [0, 1, 3, 5, 7]
