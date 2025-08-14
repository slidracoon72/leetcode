from collections import defaultdict


class Solution:
    # Solved using Sliding Window
    # Time: O(n), Space: O(n)
    def largestGoodInteger(self, num: str) -> str:
        # Dictionary to store the frequency of digits in the current sliding window
        count = defaultdict(int)

        res = ""  # Stores the largest "good integer" found so far
        big = 0  # Stores the largest digit that forms a "good integer"

        # Iterate over each character in the string
        for i in range(len(num)):
            # Increment count for the current digit
            count[num[i]] += 1

            # Maintain a sliding window of size 3
            # If window exceeds size 3, remove the oldest digit from the count
            if i - 3 >= 0:
                count[num[i - 3]] -= 1

            # Check if current digit appears exactly 3 times in the current window
            if count[num[i]] == 3:
                # If this digit is larger than the previously recorded largest digit, update result
                if int(num[i]) >= big:
                    big = int(num[i])
                    res = num[i] * 3  # Store the 3-digit string (e.g., "777")

        # Return the largest good integer found (or empty string if none found)
        return res

    # Checking for three consecutive digits
    # Time: O(n), Space: O(1)
    def largestGoodInteger1(self, num: str) -> str:
        res = ""

        # Loop through the string and check every group of 3 consecutive digits
        for i in range(len(num) - 2):
            # If all three consecutive digits are the same
            if num[i] == num[i + 1] == num[i + 2]:
                # If it's larger than the current best, update result
                if res == "" or num[i] > res[0]:
                    res = num[i] * 3

        return res


c = Solution()
print(c.largestGoodInteger("6777133339"))
print(c.largestGoodInteger("2300019"))
print(c.largestGoodInteger("42352338"))
print(c.largestGoodInteger("222"))
