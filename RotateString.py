class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if the lengths are the same
        if len(s) != len(goal):
            return False

        # Double the string s to simulate all possible rotations
        s += s
        goal_length = len(goal)

        # Use a sliding window to check for `goal` in `s + s`
        for i in range(len(s) - goal_length + 1):
            if s[i:i + goal_length] == goal:
                return True

        return False

    def rotateString1(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        return goal in (s + s)
