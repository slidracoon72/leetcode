from typing import List


class Solution:
    # Brute Force - TLE
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        d = [0] * n

        for l, r in queries:
            for i in range(l, r + 1):
                d[i] += 1

        for i in range(n):
            if nums[i] > 0:
                nums[i] -= d[i]

        return sum(nums) == 0

    # Solving using Difference Array - ideal for range updates
    # Invert the problem - Convert 0-array to nums
    # Time Complexity: O(N + Q), Space Complexity: O(N)
    def isZeroArray1(self, nums: List[int], queries: List[List[int]]) -> bool:
        # Create a difference array (delta) to track range increments
        n = len(nums)
        diff = [0] * (n + 1)

        # Apply range increment using prefix sum technique
        for start, end in queries:
            diff[start] += 1
            if end + 1 < len(diff):
                diff[end + 1] -= 1

        # Convert difference array to the actual number of operations on each index
        ops = [0] * n
        running_sum = 0
        for i in range(n):
            running_sum += diff[i]
            ops[i] = running_sum

        # Compare applied operations with target array
        for i in range(n):
            if ops[i] < nums[i]:
                return False

        return True


c = Solution()
nums = [1, 0, 1]
queries = [[0, 2]]
print(c.isZeroArray1(nums, queries))
######
nums = [4, 3, 2, 1]
queries = [[1, 3], [0, 2]]
print(c.isZeroArray1(nums, queries))
