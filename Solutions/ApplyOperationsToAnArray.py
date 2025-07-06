from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        res = []
        for x in nums:
            if x:
                res.append(x)

        for _ in range(n - len(res)):
            res.append(0)

        return res

    # Similar approach - Fixed Array
    def applyOperations1(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        result = [0] * n
        pos = 0
        for num in nums:
            if num != 0:
                result[pos] = num
                pos += 1

        return result


c = Solution()
nums = [1, 2, 2, 1, 1, 0]
print(c.applyOperations(nums))
nums = [3, 3, 2, 1, 0, 1, 0]
print(c.applyOperations1(nums))
