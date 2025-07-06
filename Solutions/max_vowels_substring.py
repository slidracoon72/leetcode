s = "aeiouuexcdvfv"
k = 9
vowels = ["a", "e", "i", "o", "u"]
# Start sliding window
l = 0
r = k
maxSum = 0
while r < len(s) + 1:
    count = 0
    for i in range(l, r):
        if s[i] in vowels:
            count += 1
            maxSum = max(maxSum, count)
    l += 1
    r += 1

# print(maxSum)


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Maximum vowels i.e. ans
        ans = 0

        # Vowels in current window
        currCount = 0

        # String of vowels
        vowels = "aeiou"

        # Using sliding window technique to
        # calculate number of vowels in each window and
        # update the count
        for i, v in enumerate(s):
            print(i, v)
            if i >= k:
                if s[i - k] in vowels:
                    currCount -= 1
            if s[i] in vowels:
                currCount += 1
            ans = max(currCount, ans)
        return ans


c = Solution()
s = "leetcode"
k = 3
print(c.maxVowels(s, k))
