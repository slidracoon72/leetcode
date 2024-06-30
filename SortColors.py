from typing import List


# Counting Sort
# Time Complexity: O(n), Space: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize a list to count occurrences of each color
        # R (red) = 0, W (white) = 1, B (blue) = 2
        colors = [0, 0, 0]

        # Count the number of occurrences of each color
        for color in nums:
            colors[color] += 1

        # Extract counts for each color
        R, W, B = colors

        # Overwrite the original array with sorted colors
        nums[:R] = [0] * R  # Fill the first R positions with 0 (red)
        nums[R: R + W] = [1] * W  # Fill the next W positions with 1 (white)
        nums[R + W:] = [2] * B  # Fill the remaining positions with 2 (blue)

        print(nums)  # Print the sorted array


nums = [2, 0, 2, 1, 2, 0]
c = Solution()
c.sortColors(nums)
