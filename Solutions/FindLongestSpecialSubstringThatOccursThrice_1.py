from collections import defaultdict


class Solution:
    # Time: O(n^2), Space: O(n^2)
    def maximumLength(self, s: str) -> int:
        # Create a dictionary to store the count of all substrings.
        count = defaultdict(int)

        for start in range(len(s)):
            character = s[start]
            substring_length = 0

            for end in range(start, len(s)):
                # If the string is empty, or the current character is equal to
                # the previously added character, then add it to the map.
                # Otherwise, break the iteration.
                if character == s[end]:
                    substring_length += 1
                    count[(character, substring_length)] += 1
                else:
                    break

        # Create a variable ans to store the longest length of substring with
        # frequency atleast 3.
        ans = 0
        for key, value in count.items():
            length = key[1]
            if value >= 3 and length > ans:
                ans = length

        if ans == 0:
            return -1
        return ans


c = Solution()
s = "aaaa"
print(c.maximumLength(s))
