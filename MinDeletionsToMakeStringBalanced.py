# Time: O(n), Space: O(n)
# Make all characters to left -> a
# Make all characters to right -> b
# Neetcode: https://www.youtube.com/watch?v=WDStNufBUQ8&t=604s
class Solution:
    def minimumDeletions(self, s: str) -> int:
        # count of 'a' to the right of each index. These 'a' are to be deleted
        a_count_right = [0] * len(s)

        # Reverse loop from second last element to stay in-bounds while checking 'i+1'
        # Populating 'a_count_right' array
        for i in range(len(s) - 2, -1, -1):
            a_count_right[i] = a_count_right[i + 1]
            if s[i + 1] == 'a':
                a_count_right[i] += 1

        # count of 'b' to the left of each index. These 'b' are to be deleted
        b_count_left = 0
        res = float('inf')
        for i, c in enumerate(s):
            deletion = b_count_left + a_count_right[i]
            res = min(res, deletion)
            if c == 'b':
                b_count_left += 1

        return res


c = Solution()
s = "aababbab"
print(c.minimumDeletions(s))
