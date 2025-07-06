# LC - Hard
from typing import List


class Solution:
    # Neetcode: https://www.youtube.com/watch?v=lB_gLotpnuY
    # Time: O(nlogn), Space: O(n)
    def putMarbles(self, weights: List[int], k: int) -> int:
        # If only one bag is needed, there is no difference in scores
        if k == 1:
            return 0

        splits = []  # List to store the sum of adjacent marble weights
        for i in range(len(weights) - 1):
            splits.append(weights[i] + weights[i + 1])  # Compute pairwise sums

        splits.sort()  # Sort the sums to easily find min and max split contributions

        i = k - 1  # We need to make (k - 1) splits to create k bags

        # Calculate the maximum score by selecting the largest (k-1) splits
        max_score = weights[0] + weights[-1] + sum(splits[-i:])

        # Calculate the minimum score by selecting the smallest (k-1) splits
        min_score = weights[0] + weights[-1] + sum(splits[:i])

        # The difference between the maximum and minimum possible scores
        return max_score - min_score


c = Solution()
weights = [1, 3, 5, 1]
k = 2
print(c.putMarbles(weights, k))
