from typing import List, Counter


class Solution:
    # Using Hash-Map
    # Time: O(nlogn), Space: O(n)
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        arr = sorted([[num, cnt] for num, cnt in c.items()])

        res = 0
        for i in range(1, len(arr)):
            prev = arr[i - 1]
            cur = arr[i]
            if cur[0] - prev[0] == 1:
                res = max(res, cur[1] + prev[1])

        return res

    # Similar as above - But Optimized
    # Time: O(n), Space: O(n)
    def findLHS1(self, nums):
        c = Counter(nums)
        res = 0

        for num in c:
            if (num + 1) in c:
                length = c[num] + c[num + 1]
                res = max(res, length)

        return res

    # Using Sliding Window
    # Time: O(nlogn), Space: O(1)
    def findLHS2(self, nums):
        # Sort the array to bring consecutive numbers closer
        nums.sort()
        res = 0  # Store the length of the longest harmonious subsequence

        l = 0  # Left pointer of the window
        for r in range(len(nums)):  # Right pointer iterates through the array
            # Shrink the window from the left if the difference is more than 1
            while nums[r] - nums[l] > 1:
                l += 1
            # If the difference is exactly 1, update the result with window size
            if nums[r] - nums[l] == 1:
                res = max(res, r - l + 1)

        return res


c = Solution()
nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(c.findLHS(nums))
