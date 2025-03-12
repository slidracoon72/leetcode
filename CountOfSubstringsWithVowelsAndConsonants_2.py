# LC - 3306. Count of Substrings Containing Every Vowel and K Consonants II
from collections import defaultdict


class Solution:
    # Sliding Window
    # Similar to NumOfSubstringsContainingAllThreeCharacters.py
    # Time: O(n), Space: O(1)
    def countOfSubstrings(self, word: str, k: int) -> int:
        """
        Count substrings in 'word' that contain all vowels ('a', 'e', 'i', 'o', 'u')
        at least once and exactly k consonants.

        Args:
            word (str): Input string of lowercase English letters.
            k (int): Exact number of consonants required in substrings.

        Returns:
            int: Number of valid substrings.
        """

        def at_least_k(k: int) -> int:
            """Helper function to count substrings with all vowels and at least k consonants."""
            # Define the set of vowels for quick lookup
            vowels = "aeiou"
            # Dictionary to track frequency of each vowel in the current window
            vowel_count = defaultdict(int)
            # Counter for consonants in the current window
            consonants = 0

            # Result: total number of substrings with at least k consonants and all vowels
            res = 0
            # Left pointer of the sliding window
            l = 0

            # Iterate with right pointer to expand the window
            for r in range(len(word)):
                # Current character at right pointer
                if word[r] in vowels:
                    # Increment count of this vowel
                    vowel_count[word[r]] += 1
                else:
                    # Increment consonant count if not a vowel
                    consonants += 1

                # Shrink window while we have at least k consonants and all 5 vowels
                while consonants >= k and len(vowel_count) == 5:
                    # Add number of substrings ending at r, starting from current l
                    # For each valid window [l, r], we can extend r to end of string
                    res += len(word) - r
                    # Process leftmost character to shrink window
                    if word[l] in vowels:
                        # Decrease vowel count
                        vowel_count[word[l]] -= 1
                        # Remove vowel from dictionary if its count becomes 0
                        if vowel_count[word[l]] == 0:
                            del vowel_count[word[l]]
                    else:
                        # Decrease consonant count if left char is a consonant
                        consonants -= 1
                    # Move left pointer to shrink window
                    l += 1

            # Return total substrings with at least k consonants
            return res

        # Total = (substrings with >= k consonants) - (substrings with >= k+1 consonants)
        # This gives us substrings with exactly k consonants
        return at_least_k(k) - at_least_k(k + 1)


c = Solution()
word = "ieaouqqieaouqq"
k = 1
print(c.countOfSubstrings(word, k))
