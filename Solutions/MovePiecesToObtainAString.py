class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Initialize two pointers for start and target strings and get the length of the strings
        i, j, n = 0, 0, len(start)

        # Iterate through both strings while there are characters left to process
        while i < n or j < n:
            # Skip all underscores in the 'start' string
            while i < n and start[i] == '_':
                i += 1
            # Skip all underscores in the 'target' string
            while j < n and target[j] == '_':
                j += 1

            # If either pointer reaches the end of its respective string, break the loop
            if i == n or j == n:
                break

            # Check if the non-underscore characters at the current positions don't match
            if start[i] != target[j]:
                return False

            # 'L' in 'start' can only move left, so 'L' in 'start' should not be to the right of 'L' in 'target'
            if start[i] == 'L' and i < j:
                return False

            # 'R' in 'start' can only move right, so 'R' in 'start' should not be to the left of 'R' in 'target'
            if start[i] == 'R' and i > j:
                return False

            # Move both pointers to the next character
            i += 1
            j += 1

        # Both pointers should reach the end of the strings simultaneously for a valid transformation
        return i == n and j == n
