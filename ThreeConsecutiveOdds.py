from typing import List


class Solution:
    # Using Sliding Window
    # Time: O(n), Space: O(1)
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # Get the length of the input array
        n = len(arr)
        # If array length is less than 3, no three consecutive odds possible
        if n < 3:
            return False

        # Initialize odd count for the first window
        odd_count = 0
        for i in range(3):
            if arr[i] % 2:
                odd_count += 1

        # Check the first window
        if odd_count == 3:
            return True

        # Slide the window from index 3 to end
        for r in range(3, len(arr)):
            # Remove the leftmost element of the previous window
            if arr[r - 3] % 2 == 1:
                odd_count -= 1
            # Add the new rightmost element
            if arr[r] % 2 == 1:
                odd_count += 1
            # Check if current window has three odds
            if odd_count == 3:
                # print(arr[r - 2: r + 1])
                return True

        return False

    # Using Counting
    # Time: O(n), Space: O(1)
    def threeConsecutiveOdds1(self, arr: List[int]) -> bool:
        # Get the length of the input array
        n = len(arr)
        # If array length is less than 3, no three consecutive odds possible
        if n < 3:
            return False

        # Initialize counter for consecutive odd numbers
        odd_count = 0

        # Iterate through each number in the array
        for num in arr:
            # Check if the number is odd using bitwise AND (1 if odd, 0 if even)
            if num & 1:
                # Increment the count of consecutive odds
                odd_count += 1
            else:
                # Reset the count when an even number is encountered
                odd_count = 0

            # If three consecutive odd numbers are found, return True
            if odd_count == 3:
                return True

        # Return False if no three consecutive odd numbers are found
        return False


c = Solution()
arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
print(c.threeConsecutiveOdds(arr))
print(c.threeConsecutiveOdds1(arr))
