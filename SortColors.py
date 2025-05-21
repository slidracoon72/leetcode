from typing import List


class Solution:
    # Counting Sort
    # Time Complexity: O(n), Space: O(1)
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

    # Three-Pointers
    # Time Complexity: O(n), Space: O(1)
    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Assign values for clarity
        red, white, blue = 0, 1, 2

        # Initialize pointers:
        # l: end of red region
        # m: current element to process
        # r: start of blue region
        l, m, r = 0, 0, n - 1

        # Process elements until middle pointer passes the right pointer
        while m <= r:
            cur = nums[m]

            if cur == red:
                # Current is red (0), swap with left boundary
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif cur == white:
                # Current is white (1), no need to swap
                m += 1
            else:
                # Current is blue (2), swap with right boundary
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1

        print(nums)  # Print the sorted array


nums = [2, 0, 2, 1, 2, 0]
c = Solution()
c.sortColors(nums)
nums = [2, 0, 1]
c.sortColors1(nums)
