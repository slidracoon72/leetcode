class Solution:
    def jump(self, nums) -> int:
        # Solving using BFS - Greedy Algorithm (Time: O(N), Space: O(1))
        jump = 0
        l = r = 0  # Two pointers for boundary of jump window

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):  # looping through the jump window
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            jump += 1

        return jump


c = Solution()
nums1 = [2, 3, 1, 1, 4]
nums2 = [2, 3, 0, 1, 4]

print(c.jump(nums1))
print(c.jump(nums2))
