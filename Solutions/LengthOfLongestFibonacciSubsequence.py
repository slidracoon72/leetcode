from typing import List


class Solution:
    # Time: O(n^2), Space: O(n)
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # Convert the input list to a set for O(1) lookup time
        arr_set = set(arr)
        n = len(arr)
        res = 0  # Variable to store the maximum length of Fibonacci-like subsequence found

        # The starting 2 numbers for a Fibonacci sequence can be any pair from the given array
        # Thus, iterate through all pairs of numbers in the array
        for i in range(n - 1):
            for j in range(i + 1, n):
                length = 2  # Every valid Fibonacci-like sequence starts with at least two numbers
                prev, curr = arr[i], arr[j]  # Initialize first two numbers of the sequence

                # Compute the next number in the sequence
                nxt = prev + curr

                # Continue to check if the next number exists in the array
                while nxt in arr_set:
                    length += 1  # Increment the sequence length
                    prev, curr = curr, nxt  # Shift the last two numbers
                    nxt = prev + curr  # Compute the new next number

                    # Update the maximum length found so far
                    res = max(res, length)

        return res  # Return the maximum length found

    # Using Dynamic Programming
    # Time: O(n^2), Space: O(n^2)
    # Neetcode: https://www.youtube.com/watch?v=33kCYPLnvcE&ab_channel=NeetCodeIO
    def lenLongestFibSubseq1(self, arr: List[int]) -> int:
        # Create a hashmap (dictionary) to store the index of each element in arr
        arr_map = {n: i for i, n in enumerate(arr)}
        n = len(arr)

        # Dictionary to store the longest Fibonacci-like subsequence starting from indices (i, j)
        dp = {}  # Key: (i, j) -> Value: length of the longest subsequence
        res = 0  # Variable to track the maximum length found

        # Iterate through the array in reverse order to populate the DP table efficiently
        for i in reversed(range(n - 1)):  # Iterate from second-last element to the first
            for j in reversed(range(i + 1, n)):  # Iterate from last element to the next of i
                length = 2  # Base case: A valid Fibonacci-like subsequence starts with 2 elements
                prev, curr = arr[i], arr[j]  # Define first two elements

                # Compute the next element in Fibonacci-like sequence
                nxt = prev + curr

                # Check if nxt exists in arr_map (i.e., if arr contains prev + curr)
                if nxt in arr_map:
                    # If found, update length using DP
                    length = 1 + dp[(j, arr_map[nxt])]  # Extend the existing sequence
                    res = max(res, length)  # Update the maximum sequence length

                # Store the computed length in dp for the pair (i, j)
                dp[(i, j)] = length

        return res  # Return the maximum length found


c = Solution()
arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
arr2 = [1, 3, 7, 11, 12, 14, 18]
print(c.lenLongestFibSubseq(arr1))
print(c.lenLongestFibSubseq1(arr1))
print(c.lenLongestFibSubseq(arr2))
print(c.lenLongestFibSubseq1(arr2))
