from typing import List


class Solution:
    # Time: O(nlogn + nlogk), Space: O(n)
    def longestSquareStreak(self, nums: List[int]) -> int:
        # Convert nums list to a set to allow O(1) lookup
        nums_set = set(nums)
        longest_streak = 0

        # Track visited elements to avoid redundant work
        visited = set()
        # Sort the unique elements to ensure we start from the smallest number
        sorted_nums = sorted(nums_set)

        for n in sorted_nums:
            # Skip numbers that have already been visited
            if n in visited:
                continue

            current_streak = 1
            current_num = n
            visited.add(n)

            # Check if the square of the current number exists in the set
            while current_num ** 2 in nums_set:
                visited.add(current_num ** 2)
                # Update current number to its square
                current_num **= 2
                current_streak += 1

            # Update the longest streak
            if current_streak > 1:
                longest_streak = max(longest_streak, current_streak)

        return longest_streak if longest_streak > 1 else -1
