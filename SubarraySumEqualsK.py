from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0  # Counts the number of subarrays with sum equal to k
        curSum = 0  # Tracks the current prefix sum

        prefixSums = defaultdict(int)  # Hashmap to store prefix sum frequencies
        prefixSums[0] = 1  # Initialize with sum 0 occurring once to handle cases where subarray starts at index 0

        for num in nums:
            curSum += num  # Update current prefix sum

            diff = curSum - k  # Check if there is a previous prefix sum such that curSum - previous = k

            # If such a prefix sum exists, it means there is a subarray ending here that sums to k
            res += prefixSums[diff]

            # Update the count of current prefix sum in hashmap
            prefixSums[curSum] += 1

        return res


c = Solution()
nums = [1, 1, 1]
k = 2
print(c.subarraySum(nums, k))
