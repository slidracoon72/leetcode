from typing import List


# Neetcode: https://www.youtube.com/watch?v=J0yYlj_oVTI
# Sliding Window
# Time: O(n), Space: O(1)

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Initialize the minimum and maximum values with the first array's first and last elements.
        cur_min, cur_max = arrays[0][0], arrays[0][-1]
        # Initialize the result variable to store the maximum distance.
        res = 0

        # Start iterating from the second array (index 1) because the first array has already been considered.
        for i in range(1, len(arrays)):
            arr = arrays[i]

            # Calculate the possible maximum distances:
            # 1. The difference between the current array's last element and the smallest element seen so far.
            # 2. The difference between the largest element seen so far and the current array's first element.
            # Update the result with the maximum of the current result and these two distances.
            res = max(
                res,
                arr[-1] - cur_min,  # Distance using the current array's max and global min.
                cur_max - arr[0]  # Distance using the global max and the current array's min.
            )

            # Update the global minimum and maximum values.
            cur_min = min(cur_min, arr[0])
            cur_max = max(cur_max, arr[-1])

        # Return the maximum distance found.
        return res


c = Solution()
# arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]
arrays = [[-2], [-3, -2, 1]]
print(c.maxDistance(arrays))
