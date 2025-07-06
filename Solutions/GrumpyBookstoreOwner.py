from typing import List


# Sliding Window
# Time: O(n), Space: O(1)
# Neetcode: https://www.youtube.com/watch?v=pXFbNuEIn8Q
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0  # Left pointer for the sliding window
        window, max_window = 0, 0  # Current window sum and maximum window sum
        satisfied = 0  # Base count of satisfied customers without the technique

        for r in range(len(customers)):  # Iterate over each minute
            if grumpy[r] == 1:  # If the owner is grumpy at minute r
                window += customers[r]  # Add grumpy minute customers to the window sum
            else:
                # Base case: add satisfied customers to the total satisfied count
                satisfied += customers[r]

            # If the window length exceeds the allowed 'minutes', slide the window
            if r - l + 1 > minutes:
                if grumpy[l] == 1:  # Only subtract customers if the left pointer was grumpy
                    window -= customers[l]
                l += 1  # Move the left pointer to the right

            # Track the maximum window sum observed
            max_window = max(window, max_window)

        # Return the total satisfied customers including the best grumpy window handled
        return satisfied + max_window


customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3

c = Solution()
print(c.maxSatisfied(customers, grumpy, minutes))
