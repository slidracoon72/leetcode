from typing import List


class Solution:
    # Greedy Solution
    # Time: O(n), Time: O(1)
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # A set to keep track of which positions (0, 1, 2) in the target triplet have been matched
        good = set()

        # Iterate over each triplet
        for t in triplets:
            # Skip triplet if any value exceeds the target at that position
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue  # Cannot use this triplet as it violates the target constraints

            # Check if any value in the triplet exactly matches the target at the same position
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)  # Mark this index as matched

        # If we have matched all three indices (0, 1, 2), return True
        return len(good) == 3


c = Solution()
triplets = [[1, 2, 3], [7, 1, 1]]
target = [7, 2, 3]
print(c.mergeTriplets(triplets, target))
