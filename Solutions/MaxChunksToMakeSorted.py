from typing import List


class Solution:
    # Time: O(n), Space: O(1)
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        max_so_far = 0  # Tracks the maximum value in the current chunk
        res = 0  # Counts the number of chunks

        for i in range(n):
            max_so_far = max(max_so_far, arr[i])  # Update the maximum value seen so far
            # If the maximum value equals the current index, we can form a chunk
            if max_so_far == i:
                res += 1

        return res


c = Solution()
arr = [1, 0, 2, 3, 4]
print(c.maxChunksToSorted(arr))
