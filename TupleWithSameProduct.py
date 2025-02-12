from typing import List
from collections import defaultdict


# Techdose Solution: https://www.youtube.com/watch?v=TBCOBD-24oE&ab_channel=Techdose
# Time: O(n^2), Space: O(n^2)
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pair_cnt = defaultdict(int)  # Dictionary to store product frequencies

        # Iterate through all possible pairs of numbers
        for i in range(n - 1):
            for j in range(i + 1, n):
                a, b = nums[i], nums[j]
                product = a * b  # Calculate the product of the pair
                pair_cnt[product] += 1  # Count occurrences of the same product

        res = 0  # Variable to store the total count of valid tuples

        # Iterate through the dictionary of product frequencies
        for pair, freq in pair_cnt.items():
            if freq > 1:
                # Calculate the number of ways to choose two pairs with the same product
                combinations = (freq * (freq - 1)) // 2  # Formula for nC2 = n(n-1)/2
                res += 8 * combinations  # Each valid combination forms 8 unique tuples

        return res  # Return the total number of valid tuples


c = Solution()
nums = [1, 2, 4, 5, 10]
print(c.tupleSameProduct(nums))
