class Solution:
    # Sliding Window - Hard
    # Time Complexity: O(N)
    # Neetcode: https://www.youtube.com/watch?v=jSto0O4AJbM
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # Initialize counters for characters in t and window
        countT, window = {}, {}

        # Count occurrences of characters in t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Initialize variables for tracking the window state and result
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')
        l = 0

        # Expand the window to the right
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # Check if the current character is in t and window has required count
            if c in countT and window[c] == countT[c]:
                have += 1

            # Contract the window from the left if all characters are found
            while have == need:
                # Update result if the current window size is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Remove leftmost character from the window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        # Extract result substring from original string
        l, r = res
        if resLen != float('inf'):
            return s[l:r + 1]
        else:
            return ""


s = "ADOBECODEBANC"
t = "ABC"
c = Solution()
print(c.minWindow(s, t))
