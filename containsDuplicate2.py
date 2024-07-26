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

    # Solved using Sliding Window
    def containsNearbyDuplicate1(self, nums, k) -> bool:
        window = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False


c = Solution()
nums = [1, 2, 3, 1, 2, 3]
k = 2
nums1 = [1, 2, 3, 1]
k1 = 3
print(c.containsNearbyDuplicate(nums1, k1))
