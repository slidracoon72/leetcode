class Solution:
    # Time: O(n), Space: O(n)
    def maxScore(self, s: str) -> int:
        res = -1
        for i in range(len(s)):
            left = s[:i]
            right = s[i:]
            if left and right:
                res = max(res, left.count("0") + right.count("1"))
        return res

    def maxScore1(self, s: str) -> int:
        # Count total ones in the string (right substring initially contains all characters)
        total_ones = s.count("1")
        max_score = 0

        left_zeros = 0
        right_ones = total_ones

        # Traverse the string and calculate the score at each split point
        for i in range(len(s) - 1):  # Exclude the last character to keep both substrings non-empty
            if s[i] == "0":
                left_zeros += 1
            else:
                right_ones -= 1
            max_score = max(max_score, left_zeros + right_ones)

        return max_score


c = Solution()
s = "011101"
print(c.maxScore(s))
print(c.maxScore1(s))
