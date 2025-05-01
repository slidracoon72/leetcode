class Solution:
    # Time: O(2^n), Space: O(2^n)
    def countAndSay(self, n: int) -> str:
        # Base case: if n is 1, return "1"
        if n == 1:
            return "1"

        # Helper function to perform run-length encoding (RLE) on string s
        def rle(s):
            new_s = ""  # Initialize the new string for the next sequence
            l = 0  # Left pointer to traverse the string
            while l < len(s):
                r = l  # Right pointer to count occurrences of the same digit
                cur = s[l]  # Current character being counted
                # Move right pointer while the same digit repeats
                while cur == s[r]:
                    r += 1
                    if r >= len(s):
                        break
                # Append the count and the digit to the new string
                new_s += str(r - l) + cur
                l = r  # Move the left pointer to the next new digit

            return new_s

        prev = "1"  # Starting string for n = 1
        # Generate the sequence up to the nth term
        for _ in range(2, n + 1):
            new_s = rle(prev)  # Get the next sequence using RLE
            prev = new_s  # Update prev for the next iteration
        return prev  # Return the nth term


c = Solution()
n = 4
print(c.countAndSay(n))
