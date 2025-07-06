from typing import List


class Solution:
    # Using Sliding Window
    # Time: O(N), Space: O(1)
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # Extend the list by appending the first (k-1) elements to handle wraparound cases
        colors = colors + colors[:k - 1]
        n = len(colors)  # Updated length after extension

        res = 0  # Counter for valid alternating groups of length >= k
        cur = 1  # Tracks the current alternating substring length

        # Iterate through the extended list
        for i in range(1, n):
            if colors[i] != colors[i - 1]:  # Check if current color is different from previous
                cur += 1  # Increase the alternating sequence length
            else:  # If not alternating, reset the counter
                cur = 1

            if cur >= k:  # If we have found a valid alternating group of at least length k
                res += 1  # Increment the result counter

        return res  # Return the total count of alternating groups of size at least k


c = Solution()
colors = [0, 1, 0, 1, 0]
k = 3
print(c.numberOfAlternatingGroups(colors, k))
