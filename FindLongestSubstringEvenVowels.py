# LC-1371: Find the Longest Substring Containing Vowels in Even Counts
class Solution:
    # Getting TLE
    # Time: O(n^3)
    def findTheLongestSubstring(self, s: str) -> int:
        size = len(s)
        res = 0

        # Iterate through all starting points of the substring
        for l in range(size):
            vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

            # Iterate through all ending points of the substring starting from l
            for r in range(l, size):
                # Check the current character and update the vowel count if it's a vowel
                if s[r] in vowels:
                    vowels[s[r]] += 1

                # Check if all vowels appear an even number of times
                if all(value % 2 == 0 for value in vowels.values()):
                    # Calculate the length of the current valid substring
                    res = max(res, r - l + 1)

        return res

    # DO AGAIN
    def findTheLongestSubstring1(self, s: str) -> int:
        mapy = [-2] * 32
        mapy[0] = -1

        max_len = 0
        mask = 0

        for i, char in enumerate(s):
            if char == 'a':
                mask ^= 1
            elif char == 'e':
                mask ^= 2
            elif char == 'i':
                mask ^= 4
            elif char == 'o':
                mask ^= 8
            elif char == 'u':
                mask ^= 16

            prev = mapy[mask]
            if prev == -2:
                mapy[mask] = i
            else:
                max_len = max(max_len, i - prev)

        return max_len
