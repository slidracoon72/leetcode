from typing import List
from collections import Counter


class Solution:
    # Using Hash-Map
    # Time Complexity: O(n), Space Complexity: O(n)
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Count the frequency of each number in the nums list
        c = Counter(nums)
        # Initialize a variable to keep track of the number of operations
        count = 0
        # A set to keep track of the numbers we have already processed
        seen = set()

        # Iterate over each unique number in the counter
        for x in c:
            # If the number and its complement (k-x) haven't been processed yet
            if x not in seen and (k - x) in c:
                # If the number is exactly half of k (e.g., k=6, x=3),
                # we can only form pairs within the same number
                if x == (k - x):
                    # Count how many pairs we can form with x
                    count += c[x] // 2
                else:
                    # Count how many pairs we can form with x and k-x
                    count += min(c[x], c[k - x])

                # Add both the number and its complement to the seen set
                seen.add(x)
                seen.add(k - x)

        # Return the total number of operations
        return count

    # Using Two-Pointers
    # Time Complexity: O(nlogn), Space Complexity: O(1)
    def maxOperations1(self, nums: List[int], k: int) -> int:
        # Sort the array
        nums.sort()

        # Initialize two pointers
        left, right = 0, len(nums) - 1
        count = 0

        # Use two pointers to find pairs that sum up to k
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == k:
                # Found a pair, increment the count
                count += 1
                # Move both pointers inward
                left += 1
                right -= 1
            elif current_sum < k:
                # Sum is less than k, move the left pointer to the right
                left += 1
            else:
                # Sum is greater than k, move the right pointer to the left
                right -= 1

        return count


c = Solution()
nums = [3, 1, 3, 4, 3]
k = 6
print(c.maxOperations1(nums, k))
