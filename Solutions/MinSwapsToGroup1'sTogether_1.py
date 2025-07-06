from typing import List


# Sliding Window
# Time: O(n), Space: O(1)
# Neetcode: https://www.youtube.com/watch?v=BueoreUIkcE
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Get the length of the input list
        length = len(nums)

        # Count the total number of 1s in the list
        count_ones = nums.count(1)

        # Initialize variables to keep track of the number of 1s in the current window
        # and the maximum number of 1s found in any window
        window_ones = max_window_ones = 0

        # Left pointer of the sliding window
        l = 0

        # Since the array is circular, we iterate it until it's length * 2
        # Eg. if nums = [0,1,0,1,1], then the circular array is [0,1,0,1,1 + [0,1,0,1,1]
        # Index: 0 1 2 3 4 5 6 7 8 9
        # Value: 0 1 0 1 1 0 1 0 1 1
        # In value, any subarray of length = 5 is part of the circular array
        # Value at index 9 is the same as value at index 4 (9 % 5)

        # Iterate over the array using the right pointer
        for r in range(2 * length):
            # Add the value at the right pointer to the window_ones count if it is 1
            if nums[r % length] == 1:
                window_ones += 1

            # If the window size exceeds the count of 1s, slide the window from the left
            if r - l + 1 > count_ones:
                # Subtract the value at the left pointer from the window_ones count if it is 1
                window_ones -= nums[l % length]
                # Move the left pointer to the right
                l += 1

            # Update the maximum number of 1s found in any window
            max_window_ones = max(max_window_ones, window_ones)

        # Calculate the minimum number of swaps required
        # This is the difference between the total number of 1s and the maximum number of 1s in any window
        return count_ones - max_window_ones


c = Solution()
nums = [0, 1, 1, 1, 0, 0, 1, 1, 0]
print(c.minSwaps(nums))
