class Solution:
    # Neetcode: https://www.youtube.com/watch?v=r_3a0oG1VcY
    # Time: O(n), Space: O(n)
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Helper function to remove adjacent pairs and calculate gain
        def remove_pairs(pair, score):
            nonlocal s  # Allows modification of the outer 's'
            stack = []  # Stack to build the new string while checking for pairs
            res = 0  # Score accumulated by removing pairs

            for c in s:
                # Check if the top of the stack and current char form the desired pair
                if c == pair[1] and stack and stack[-1] == pair[0]:
                    stack.pop()  # Remove the matching pair
                    res += score  # Add the score for this pair
                else:
                    stack.append(c)  # Add current character to stack if no match

            s = "".join(stack)  # Update s with the remaining characters after removal
            return res  # Return the score from removing this type of pair

        res = 0
        # Decide which pair to remove first: the one with the higher score
        pair = "ab" if x > y else "ba"

        # First remove the higher-scoring pairs
        res += remove_pairs(pair, max(x, y))

        # Then remove the lower-scoring pairs from the remaining string
        res += remove_pairs(pair[::-1], min(x, y))

        return res  # Return the total score from all removals


c = Solution()
s = "cdbcbbaaabab"
x = 4
y = 5
print(c.maximumGain(s, x, y))
