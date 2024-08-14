from collections import defaultdict


# Citadel - OA Question
class Solution:
    def findConsistentLogs(self, userEvent):
        # Step 1: Calculate the frequency of each user in the entire array
        total_freq = defaultdict(int)
        for user in userEvent:
            total_freq[user] += 1

        # Step 2: Find the minimum frequency of any user
        min_freq = min(total_freq.values())

        # Step 3: Initialize variables for sliding window approach
        max_length = 0
        current_freq = defaultdict(int)
        l = 0

        # Traverse the array with the right pointer
        for r in range(len(userEvent)):
            current_freq[userEvent[r]] += 1

            # Adjust the left pointer to ensure the subarray is valid
            while True:
                max_freq_in_window = max(current_freq.values(), default=0)

                if max_freq_in_window == min_freq:
                    # Update max length if the current window is valid
                    max_length = max(max_length, r - l + 1)
                    break
                elif max_freq_in_window < min_freq:
                    # Extend the window to the right
                    break
                else:
                    # Remove the leftmost element and adjust frequency counts
                    current_freq[userEvent[l]] -= 1
                    if current_freq[userEvent[l]] == 0:
                        del current_freq[userEvent[l]]
                    l += 1

        return max_length


c = Solution()
# userEvent = [1, 2, 1, 3, 4, 2, 4, 3, 3, 4]
# userEvent = [9, 9, 9]
userEvent = [9, 8, 5, 9, 2]
print(c.findConsistentLogs(userEvent))
