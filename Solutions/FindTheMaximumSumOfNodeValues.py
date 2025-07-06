# LC - Hard

from typing import List


class Solution:
    # Neetcode: https://www.youtube.com/watch?v=bnBp6_b4GCw&ab_channel=NeetCodeIO
    # Time: O(nlogn), Space: O(n)
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # Step 1: Calculate the delta for each node.
        # delta[i] = (nums[i] ^ k) - nums[i]
        # This tells us how much value we gain (or lose) if we flip nums[i] using XOR with k.
        delta = [(n ^ k) - n for n in nums]

        # Step 2: Sort the deltas in descending order.
        # We'll use the largest positive deltas in pairs to maximize the total sum.
        delta.sort(reverse=True)

        n = len(nums)
        # Step 3: Start with the sum of the original array.
        res = sum(nums)

        # Step 4: Iterate through the deltas in pairs (0&1, 2&3, ...)
        # Each pair represents two nodes we can flip simultaneously.
        for i in range(0, n, 2):
            # If we reach the last unmatched node (odd number of elements), break
            if i == n - 1:
                break

            # Calculate the combined delta of the current pair
            path_delta = delta[i] + delta[i + 1]

            # If the total benefit of flipping this pair is negative, stop.
            # Further flips would reduce the total sum.
            if path_delta < 0:
                break

            # Add the benefit from this pair to the result
            res += path_delta

        # Step 5: Return the maximum possible sum after optimal flips
        return res


c = Solution()
nums = [1, 2, 1]
k = 3
edges = [[0, 1], [0, 2]]
print(c.maximumValueSum(nums, k, edges))