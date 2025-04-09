from typing import List


class Solution:
    # Recursion + Memoization - Gives MLE
    # Time: O(2^n), Space: O(n * target)
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # If the total is odd, we can't split it equally
        if total % 2 != 0:
            return False

        target = total // 2
        memo = {}

        def dfs(i, cur_sum):
            # If we've reached the target, return True
            if cur_sum == target:
                return True
            # If we exceed the target or run out of elements, return False
            if cur_sum > target or i == len(nums):
                return False
            # Memoization check
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]

            # Include or skip the current number
            include = dfs(i + 1, cur_sum + nums[i])
            skip = dfs(i + 1, cur_sum)

            memo[(i, cur_sum)] = include or skip
            return memo[(i, cur_sum)]

        return dfs(0, 0)

    # Dynamic Programming
    # Neetcode: https://www.youtube.com/watch?v=snue4L5WrJ4
    # Time: O(n*s), Space: O(s)
    def canPartition1(self, nums: List[int]) -> bool:
        total = sum(nums)

        # If the total sum is odd, it can't be partitioned into two equal subsets
        if total % 2 != 0:
            return False

        target = total // 2
        dp = set()
        dp.add(0)  # base case: zero sum is always achievable with an empty subset

        # Iterate over each number in reverse
        for i in range(len(nums) - 1, -1, -1):
            next_dp = dp.copy()  # copy current achievable sums
            for t in dp:
                temp = t + nums[i]  # try adding the current number to each existing sum
                if temp == target:
                    return True  # early exit if we can already form the target sum
                next_dp.add(temp)  # add new sum to the set
            dp = next_dp  # update dp with new possible sums

        # Final check if target is in the set of achievable sums
        return target in dp


c = Solution()
nums = [1, 5, 11, 5]
print(c.canPartition(nums))
print(c.canPartition1(nums))
