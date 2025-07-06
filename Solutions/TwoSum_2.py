from typing import List


# Solved using Binary Search (Two-Pointers)
# Time: O(logn), Space: O(logn)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, e = 0, len(numbers) - 1
        while s < e:
            temp = numbers[s] + numbers[e]
            if temp == target:
                return [s + 1, e + 1]
            elif temp < target:
                s += 1
            else:
                e -= 1
        return []

    # Similar as above
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            temp = nums[l] + nums[r]
            if temp > target:
                r -= 1
            elif temp < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []

    def twoSum_alternate(self, numbers: List[int], target: int) -> List[int]:
        s, f = 0, 1
        while f < len(numbers):
            temp = numbers[s] + numbers[f]
            if temp == target:
                return [s + 1, f + 1]
            elif temp < target:
                f += 1
            else:
                s += 1
                f = s + 1
        return []  # Return empty list if no such pair is found


c = Solution()
numbers = [3, 24, 50, 79, 88, 150, 345]
target = 200
print(c.twoSum(numbers, target))
print(c.twoSum_alternate(numbers, target))
