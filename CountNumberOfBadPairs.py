from collections import defaultdict
from typing import List


class Solution:
    # Brute Force - Gives TLE
    # Time: O(n^2), Space: O(1)
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if i < j and j - i != nums[j] - nums[i]:
                    res += 1
        return res

    # Optimal Solution - https://www.youtube.com/watch?v=KCi1uoHdeLs&ab_channel=Techdose
    # Time: O(N), Space: O(N)
    def countBadPairs1(self, nums: List[int]) -> int:
        n = len(nums)  # Get the length of the input list
        total_pairs = (n * (n - 1)) // 2  # Calculate the total number of possible pairs (n choose 2)
        good_pairs = 0  # Initialize a counter for the number of good pairs

        # Create a dictionary to track occurrences of (nums[i] - i) values
        freq = defaultdict(int)

        # Iterate through the list of numbers and their indices
        # Count good pairs: nums[i] - i == nums[j] - j
        for i, x in enumerate(nums):
            # Check if the difference (x - i) has appeared before
            if x - i in freq:
                # If it has, increment the count of good pairs by the frequency of this difference
                good_pairs += freq[x - i]

            # Update the frequency of the current (x - i) difference
            freq[x - i] += 1

        # The number of bad pairs is the total pairs minus the good pairs
        bad_pairs = total_pairs - good_pairs
        return bad_pairs  # Return the number of bad pairs


c = Solution()
nums = [4, 1, 3, 3]
print(c.countBadPairs1(nums))
