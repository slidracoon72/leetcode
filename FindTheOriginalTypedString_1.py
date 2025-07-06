class Solution:
    # Time: O(n), Space: O(1)
    def possibleStringCount(self, word: str) -> int:
        # Initialize the result with 1 because the original string itself is a valid possibility
        res = 1

        # Loop through the string starting from the second character
        for i in range(1, len(word)):
            # If the current character is the same as the previous character
            # then increment the result count
            if word[i - 1] == word[i]:
                res += 1

        # Return the total count of possible strings based on the rule
        return res


c = Solution()
word = "abbcccc"
print(c.possibleStringCount(word))
