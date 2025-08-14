from collections import defaultdict
from typing import List


class Solution:
    # Sliding Window
    # Time: O(n), Space: O(1)
    def totalFruit(self, fruits: List[int]) -> int:
        # Get the length of the input array
        n = len(fruits)
        # Initialize variable to store the maximum length of valid subarray
        res = 0

        # Use defaultdict to track frequency of fruit types in the current window
        basket = defaultdict(int)
        # Initialize left pointer for the sliding window
        l = 0
        # Iterate through the array with right pointer
        for r in range(n):
            # Add current fruit to the basket and increment its count
            basket[fruits[r]] += 1

            # Shrink window while there are more than 2 fruit types
            while len(basket) > 2:
                # Decrease count of the fruit at the left pointer
                basket[fruits[l]] -= 1
                # Remove fruit type from basket if its count becomes 0
                if not basket[fruits[l]]:
                    del basket[fruits[l]]
                # Move left pointer to shrink the window
                l += 1

            # Update max length of subarray with at most 2 fruit types
            res = max(res, r - l + 1)

        # Return the maximum length found
        return res


c = Solution()
fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
print(c.totalFruit(fruits))
