from typing import List


class Solution:
    # Time: O(n^2), Space: O(1)
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0  # To count the number of unplaced fruits
        n = len(baskets)  # Total number of baskets

        # Iterate through each fruit
        for fruit in fruits:
            unset = 1  # Assume the fruit is unplaced initially

            # Try to place the fruit in a suitable basket
            for i in range(n):
                # If the basket can hold the fruit
                if fruit <= baskets[i]:
                    baskets[i] = 0  # Mark the basket as used
                    unset = 0  # Fruit has been placed
                    break  # Move on to the next fruit

            count += unset  # If unset is still 1, the fruit couldn't be placed

        return count  # Return the total number of unplaced fruits


c = Solution()
fruits = [4, 2, 5]
baskets = [3, 5, 4]
print(c.numOfUnplacedFruits(fruits, baskets))
