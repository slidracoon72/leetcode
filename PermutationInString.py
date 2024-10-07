from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        l = len(s1)
        i = 0
        while i < len(s2) - l + 1:
            x = s2[i:i + l]
            if c == Counter(x):
                return True
            i += 1
        return False

    def checkInclusion1(self, s1: str, s2: str) -> bool:
        # Edge case: if s1 is longer than s2, no permutation is possible
        if len(s1) > len(s2):
            return False

        # Get the frequency count of characters in s1
        s1_count = Counter(s1)
        # Initialize a counter for the sliding window of size len(s1)
        window_count = Counter(s2[:len(s1)])

        # If the initial window matches, return True
        if s1_count == window_count:
            return True

        # Start sliding the window over s2
        for i in range(len(s1), len(s2)):
            # Add the current character to the window
            window_count[s2[i]] += 1
            # Remove the leftmost character of the previous window
            window_count[s2[i - len(s1)]] -= 1

            # Remove characters with 0 count to keep the counter clean
            if window_count[s2[i - len(s1)]] == 0:
                del window_count[s2[i - len(s1)]]

            # Check if the current window matches s1's count
            if s1_count == window_count:
                return True

        # No permutation match found
        return False
