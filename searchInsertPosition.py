from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)


c = Solution()
a = [1, 3, 5, 6]
t1, t2, t3 = 5, 2, 7

# print(c.search_insert(a,t1))
# print(c.search_insert(a,t2))
print(c.search_insert(a,t3))

