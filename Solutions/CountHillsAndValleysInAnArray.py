from typing import List


class Solution:
    # Time: O(n), Space: O(n)
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        res = set()  # Set to store unique (i, j) pairs that represent distinct hills/valleys

        for x in range(1, n - 1):  # Loop through each index, skipping the first and last elements
            cur = nums[x]  # Current value at index x
            i, j = x - 1, x + 1  # Initialize left and right pointers

            # Move left pointer to the closest non-equal neighbor
            while i >= 0 and nums[i] == cur:
                i -= 1

            # Move right pointer to the closest non-equal neighbor
            while j < n and nums[j] == cur:
                j += 1

            # Ensure both left and right non-equal neighbors exist
            if i >= 0 and j < n:
                # Check if the current number is greater than both neighbors (hill)
                if nums[i] < cur and cur > nums[j]:
                    res.add((i, j))  # Add unique hill segment to the set

                # Check if the current number is smaller than both neighbors (valley)
                elif nums[i] > cur and cur < nums[j]:
                    res.add((i, j))  # Add unique valley segment to the set

        return len(res)  # Return the count of unique hills and valleys

    # Pre-Processing to remove duplicates - More Optimal
    # Time: O(n), Space: O(n)
    def countHillValley1(self, nums: List[int]) -> int:
        # Step 1: Remove consecutive duplicates since they belong to the same hill/valley
        clean_nums = [nums[0]]
        for num in nums[1:]:
            if num != clean_nums[-1]:
                clean_nums.append(num)

        count = 0

        # Step 2: Loop through internal elements only (must have left and right neighbors)
        for i in range(1, len(clean_nums) - 1):
            left = clean_nums[i - 1]
            center = clean_nums[i]
            right = clean_nums[i + 1]

            # Step 3: Check if current index is part of a hill or valley
            if center > left and center > right:
                count += 1  # Hill
            elif center < left and center < right:
                count += 1  # Valley

        return count


c = Solution()
nums = [2, 4, 1, 1, 6, 5]
print(c.countHillValley(nums))
