from typing import List


class Solution:
    # Time: O(n), Space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = dict()
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if num in complementMap:
                return [complementMap[num], i]
            else:
                complementMap[complement] = i

    # Similar as above
    # Time: O(n), Space: O(n)
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        complementMap = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in complementMap:
                return [complementMap[complement], i]
            else:
                complementMap[num] = i

    # Time: O(n^2)
    def bruteForceTwoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]


sol = Solution()
a1 = [1, 2, 5, 9]
t1 = 10
a2 = [2, 7, 11, 15]
t2 = 17

print("Optimal: ", sol.twoSum(a1, t1))
print("Brute Force: ", sol.bruteForceTwoSum(a2, t2))
