from typing import List


# Using Dynamic Programming
# Similar to House Robber 1 which has a linear array
# This question has a circular array
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:  # Empty array case
            return 0
        if len(nums) == 1:  # Single house case
            return nums[0]

        # Helper function for House Robber I logic
        def rob_linear(arr):
            rob1, rob2 = 0, 0  # rob1: prev house, rob2: current max
            # [rob1, rob2, n, n+1, ...]
            for num in arr:
                # Max of robbing current house + prev, or skipping current
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        # Case 1: Exclude last house (0 to n-2)
        max1 = rob_linear(nums[:-1])
        # Case 2: Exclude first house (1 to n-1)
        max2 = rob_linear(nums[1:])

        # Return maximum of the two cases
        return max(max1, max2)


c = Solution()
nums = [1, 2, 3, 1]
print(c.rob(nums))
