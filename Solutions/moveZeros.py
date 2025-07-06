class Solution:
    def moveZeroes(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums


sol = Solution()
a = [0, 1, 0, 3, 12]
b = [0, 1, 0]
c = [1, 0, 1, 0]
print(sol.moveZeroes(a))
print(sol.moveZeroes(b))
print(sol.moveZeroes(c))
