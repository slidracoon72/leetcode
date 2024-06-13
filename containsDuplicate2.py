class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                print(dic)
                return True
            dic[v] = i
        print(dic)
        return False


c = Solution()
nums = [1, 2, 3, 1, 2, 3]
k = 2
nums1 = [1, 2, 3, 1]
k1 = 3
print(c.containsNearbyDuplicate(nums1, k1))
