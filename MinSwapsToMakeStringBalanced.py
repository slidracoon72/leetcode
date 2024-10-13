class Solution:
    def minSwaps(self, s: str) -> int:
        # Variables to keep track of the number of opened and closed brackets
        opened, closed = 0, 0
        # Counter to track the number of swaps needed
        swaps = 0

        # Iterate through each character in the string
        for x in s:
            if x == '[':
                # If it's an opening bracket, increment the opened count
                opened += 1
            else:
                # If it's a closing bracket, increment the closed count
                closed += 1
                # If closed brackets exceed opened ones, a swap is needed
                if closed > opened:
                    # Increment the swap counter
                    swaps += 1
                    # Adjust the opened and closed counts after the swap
                    opened += 1  # Simulating an open bracket being placed
                    closed -= 1  # Removing the problematic closing bracket

        # Return the number of swaps needed to balance the string
        return swaps
