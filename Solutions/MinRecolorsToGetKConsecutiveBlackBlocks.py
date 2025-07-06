class Solution:
    # Invert the problem. Find a window with minimum white so the changes to be made are minimum
    # Time: O(n), Space: O(1)
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)  # Length of the string
        res = float('inf')  # Initialize result with a large value
        white = 0  # Count of 'W' (white blocks) in the current window
        l = 0  # Left pointer for the sliding window

        # Iterate through the string with a right pointer
        for r in range(n):
            if blocks[r] == "W":  # If the current block is 'W', increase count
                white += 1

            # When the window size reaches k
            if r - l + 1 >= k:
                res = min(res, white)  # Update the minimum number of white blocks to recolor

                # If the leftmost block is 'W', decrement count before moving window
                if blocks[l] == "W":
                    white -= 1

                l += 1  # Shrink the window from the left

        return res  # Return the minimum number of recolors needed


c = Solution()
blocks = "WBBWWBBWBW"
k = 7
print(c.minimumRecolors(blocks, k))
