# LC:1498 - Number of Subsequences That Satisfy the Given Sum Condition

from typing import List


class Solution:
    # Two-Pointer / Binary Search
    # Time: O(nlogn), Space: O(n)
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7

        n = len(nums)
        nums.sort()  # Sort the array to use two pointers technique

        # Precompute powers of 2 up to n for quick lookup
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        res = 0  # Initialize result count
        l, r = 0, n - 1  # Two pointers: left and right

        # Iterate until the two pointers meet - Binary Search
        while l <= r:
            # Check if the smallest + largest number is within the target
            if nums[l] + nums[r] > target:
                # If not, decrease the larger value
                r -= 1
            else:
                # If valid, all subsequences between l and r (with l as min and any combination
                # of elements between l+1 and r) are valid
                res = (res + pow2[r - l]) % MOD
                l += 1  # Move left pointer to check next smallest number

        return res


c = Solution()
print(c.numSubseq(nums=[3, 5, 6, 7], target=9))
