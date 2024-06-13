from typing import List


class Solution:
    # Kaden's Algorithm
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for i in range(1, n):
            # Update max_product and min_product by considering the possibility of negative numbers
            if nums[i] < 0:
                max_product, min_product = min_product, max_product

            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])

            # Update the result with the maximum product found so far
            result = max(result, max_product)

        return result


# nums = [2, 3, -2, 4]
# nums = [-2, 0, -1]
nums = [-2, 3, -4]
c = Solution()
print(c.maxProduct(nums))
