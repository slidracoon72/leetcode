class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()

        return newStr == newStr[::-1]  # [::-1] reverses a string

    # Using Two-Pointers
    # Time: O(n), Space: O(1)
    def isPalindromeTwoPointer(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    # helper function to find out if the character is alphanumeric or not
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))

    # Similar as above. Using built-in isalnum()
    def isPalindrome1(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


c = Solution()
print(c.isPalindrome("A man, a plan, a canal: Panama"))
print(c.isPalindromeTwoPointer("race a car"))
print(c.isPalindrome(" "))
