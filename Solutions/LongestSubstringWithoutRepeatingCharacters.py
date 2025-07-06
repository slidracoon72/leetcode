class Solution:
    # Using Sliding Window (left and right pointers)
    # Time: O(N), Space: O(M) where M = unique chars
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0

        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res


c = Solution()
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
print(c.lengthOfLongestSubstring(s1))
print(c.lengthOfLongestSubstring(s2))
print(c.lengthOfLongestSubstring(s3))
