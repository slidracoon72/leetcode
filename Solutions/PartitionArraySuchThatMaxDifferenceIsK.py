# LC:2294 - Partition Array Such That Maximum Difference Is K

class Solution:
    # Time: O(nlogn), Space: O(1)
    def partitionArray(self, nums: list[int], k: int) -> int:
        # Sort the array to make it easier to group elements based on the difference
        nums.sort()

        res = 1  # Start with one group
        prev = nums[0]  # First element of the current group

        for i in range(1, len(nums)):
            # If the current number is too far from the start of the current group
            if nums[i] - prev > k:
                res += 1  # Start a new group
                prev = nums[i]  # Update the starting point for the new group

        return res  # Return the total number of groups formed


c = Solution()
nums = [3, 6, 1, 2, 5]
k = 2
print(c.partitionArray(nums, k))
