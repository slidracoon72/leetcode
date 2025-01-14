class Solution:
    # Neetcode: https://www.youtube.com/watch?v=KMIIGDiXLhY&ab_channel=NeetCodeIO
    # Time: O(n), Space: O(n)
    def canBeValid(self, s: str, locked: str) -> bool:
        # Stack to track indices of locked '(' characters
        stack_locked = []
        # Stack to track indices of unlocked characters, which can be either '(' or ')'
        stack_unlocked = []

        # Traverse the string to match closing parentheses
        for i in range(len(s)):
            if locked[i] == "0":
                # If character is unlocked ('0'), add its index to the unlocked stack
                stack_unlocked.append(i)
            elif s[i] == "(":
                # If character is a locked '(', add its index to the locked stack
                stack_locked.append(i)
            else:
                # Handle a locked ')' character
                if stack_locked:
                    # Pop from the locked stack if there is a matching '('
                    stack_locked.pop()
                elif stack_unlocked:
                    # Use an unlocked character if no locked '(' is available
                    stack_unlocked.pop()
                else:
                    # If no matching '(' is found, return False
                    return False

        # Match remaining locked '(' with unlocked characters
        while stack_locked and stack_unlocked and stack_locked[-1] < stack_unlocked[-1]:
            stack_locked.pop()
            stack_unlocked.pop()

        # If there are unmatched locked '(', return False
        if stack_locked:
            return False

        # Check if the remaining unlocked characters can form valid pairs
        return len(stack_unlocked) % 2 == 0


c = Solution()
s = "))()))"
locked = "010100"
print(c.canBeValid(s, locked))
