from typing import List


class Solution:
    # Time: O(n), Space: O(n)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates the array 'nums' to the right by 'k' steps.
        This modifies the input list 'nums' in-place.
        """

        # Get the length of the input list
        n = len(nums)

        # Create a temporary list of the same size to hold rotated elements
        temp = [0] * n

        # Place each element from 'nums' into its rotated position in 'temp'
        for i in range(n):
            temp[(i + k) % n] = nums[i]
            # (i + k) % n ensures the index wraps around if it exceeds the array length

        # Copy the rotated elements back to the original list 'nums'
        nums[:] = temp  # Using nums[:] ensures in-place modification


c = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(c.rotate(nums, k))
