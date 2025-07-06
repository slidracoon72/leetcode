from typing import List


class Solution:
    # Time: O(nlogn), Space: O(n)
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # Intuition: To divide nums into groups of 3 with max-min difference <= k,
        # sorting nums ensures elements in each group are as close as possible.
        # Check if each group of 3 consecutive elements satisfies the condition.

        # Approach:
        # 1. Sort nums to group nearby elements.
        # 2. Iterate in steps of 3 to form groups.
        # 3. For each group, check if max-min <= k (i.e., nums[i+2] - nums[i] <= k).
        # 4. If any group fails, return empty list; else, add group to result.

        n = len(nums)  # Get length of nums
        nums.sort()  # Sort nums to minimize differences within groups
        res = []  # Initialize result list to store groups

        # Iterate over indices in steps of 3 to form groups
        for i in range(0, n, 3):
            # Check if max-min difference in group exceeds k
            if nums[i + 2] - nums[i] > k:
                return []  # Impossible to form valid groups, return empty list
            # Add valid group of 3 elements to result
            res.append([nums[i], nums[i + 1], nums[i + 2]])

        # Return list of groups
        return res


c = Solution()
nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
k = 2
print(c.divideArray(nums, k))
