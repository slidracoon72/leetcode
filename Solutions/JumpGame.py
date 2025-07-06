class Solution:
    def canJump(self, nums) -> bool:
        # Greedy Algorithm (Time: O(N), Space: O(1))
        # Start from goal, go to first index
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0


c = Solution()
nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]
print(c.canJump(nums1))
print(c.canJump(nums2))
