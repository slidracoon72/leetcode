from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return max(d, key=d.get)

    def majorityElement1(self, nums):
        nums.sort()
        print(nums)
        print("Most:", len(nums) // 2)
        return nums[len(nums) // 2]


c = Solution()
a1 = [3, 2, 3]
a2 = [2, 2, 1, 1, 1, 2, 2]

print(c.majorityElement(a1))
print(c.majorityElement(a2))
print(c.majorityElement1(a2))

print(7 // 2)
# In Python, the // operator is used for floor division, which means
# it returns the quotient of dividing the first operand by the second
# operand, rounded down to the nearest integer.
