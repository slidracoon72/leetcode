from typing import List


# Sliding Window
class Solution:
    # Optimal
    # Time: O(n), Space: O(1)
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        cons_cnt = 1

        for r in range(len(nums)):
            # Check for consecutive elements
            if r > 0 and nums[r - 1] + 1 == nums[r]:
                cons_cnt += 1

            # Shrink window if it's greater than k
            if r - l + 1 > k:
                # Update const_cnt if nums[l] is consecutive
                if nums[l] + 1 == nums[l + 1]:
                    cons_cnt -= 1
                l += 1

            if r - l + 1 == k:
                res.append(nums[r] if cons_cnt == k else -1)

        return res

    # Brute Force
    # Time: O(n*k), Space: O(1)
    def resultsArray1(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * (len(nums) - k + 1)

        def consecutive_and_sorted(arr):
            for i in range(len(arr) - 1):
                if arr[i + 1] - arr[i] != 1:
                    return False
            return True

        for i in range(len(nums) - k + 1):
            cur = nums[i: i + k]
            if consecutive_and_sorted(cur):
                res[i] = cur[-1]

        return res
