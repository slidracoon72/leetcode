from typing import List


class Solution:
    # Using Dynamic Lists
    # Time: O(n), Space: O(n)
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, right = [], []  # Dynamic Array - occupies more space
        count = 0  # count of pivot elements

        for n in nums:
            if n < pivot:
                left.append(n)
            elif n > pivot:
                right.append(n)
            else:
                count += 1

        return left + [pivot] * count + right

    # Two Passes With Fixed Array
    # Time: O(n), Space: O(1)
    def pivotArray1(self, nums, pivot):
        less = 0
        equal = 0

        for num in nums:
            if num < pivot:
                less += 1
            elif num == pivot:
                equal += 1

        ans = [0] * len(nums)  # fixed array - part of answer, so O(1) space
        lessI = 0
        equalI = less
        greaterI = less + equal

        for num in nums:
            if num < pivot:
                ans[lessI] = num
                lessI += 1
            elif num > pivot:
                ans[greaterI] = num
                greaterI += 1
            else:
                ans[equalI] = num
                equalI += 1

        return ans

    # Single Pass - With Fixed Array
    # Time: O(n), Space: O(1)
    def pivotArray2(self, nums, pivot):
        ans = [0] * len(nums)
        less_i = 0
        greater_i = len(nums) - 1

        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[i] < pivot:
                ans[less_i] = nums[i]
                less_i += 1
            if nums[j] > pivot:
                ans[greater_i] = nums[j]
                greater_i -= 1

        while less_i <= greater_i:
            ans[less_i] = pivot
            less_i += 1

        return ans


c = Solution()
nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10
print(c.pivotArray(nums, pivot))
print(c.pivotArray1(nums, pivot))
print(c.pivotArray2(nums, pivot))
