class Solution:
    # Hash Table + Enumeration
    # Time: O(n + c^2), Space: O(c); n = len(word), c = len(set(word))
    def minimumDeletions(self, word: str, k: int) -> int:
        # Intuition: To make character frequencies differ by at most k, try each
        # character's frequency as the minimum frequency, calculate deletions needed
        # to adjust other frequencies, and find the minimum deletions across all cases.

        # Approach:
        # 1. Count frequency of each character in word using a dictionary.
        # 2. For each character's frequency (f1), calculate deletions needed:
        #    - If another frequency f2 < f1, delete all f2 occurrences.
        #    - If f2 > f1 and f2 - f1 > k, delete (f2 - f1 - k) occurrences.
        # 3. Track minimum deletions across all possible minimum frequencies.

        n = len(word)  # Length of word
        freq = {}  # Dictionary to store character frequencies
        for c in word:
            freq[c] = freq.get(c, 0) + 1  # Count frequency of each character

        ans = n  # Initialize answer as worst case (delete all characters)
        for min_char, f1 in freq.items():  # Try each frequency as minimum
            del_count = 0  # Deletions needed for this minimum frequency
            for curr_char, f2 in freq.items():  # Check other frequencies
                diff = f2 - f1  # Difference between frequencies
                if f1 > f2:
                    del_count += f2  # Delete all occurrences if f2 < f1
                elif diff > k:
                    del_count += (f2 - f1 - k)  # Delete excess to make diff <= k
            ans = min(ans, del_count)  # Update minimum deletions

        return ans  # Return minimum deletions needed


c = Solution()
word = "aabcaba"
k = 0
print(c.minimumDeletions(word, k))
