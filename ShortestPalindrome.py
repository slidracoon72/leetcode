# LC - Hard


class Solution:
    # Brute Force Solution
    # The goal is to find the longest palindrome starting from the beginning of the string.
    # Once found, we reverse the remaining characters (those to the right of the palindrome)
    # and prepend them to the original string to make it a palindrome.
    # Time Complexity: O(n^2) in the worst case (checking all possible palindromes).
    # Space Complexity: O(n) for storing the result and reversed substring.

    def shortestPalindrome(self, s: str) -> str:

        # Helper function to check if a substring is a palindrome
        # Takes the string 's', and two indices 'l' and 'r', and checks if the substring s[l:r+1] is a palindrome
        def is_pali(s, l, r):
            while l <= r:
                if s[l] != s[r]:  # If characters at current indices don't match, it's not a palindrome
                    return False
                l, r = l + 1, r - 1  # Move pointers towards the center
            return True  # If no mismatches found, it's a palindrome

        # Iterate from the end of the string to the start to find the longest palindrome starting at index 0
        for r in reversed(range(len(s))):
            if is_pali(s, 0, r):  # Check if the substring from 0 to r is a palindrome
                suffix = s[r + 1:]  # The part of the string after the palindrome
                return suffix[::-1] + s  # Reverse the suffix and prepend it to the original string

        return ""  # In case the string is empty or no palindrome is found (this case won't occur due to the nature of the problem)

    # Rabin Karp Algorithm
    def shortestPalindrome1(self, s: str) -> str:
        # Initialize variables to store hash values for prefix and suffix,
        # base for polynomial hashing, last matching index, power of base, and modulus for avoiding overflow.
        prefix = 0  # Rolling hash for the prefix
        suffix = 0  # Rolling hash for the suffix
        base = 29  # Base used for hashing (commonly a prime number)
        last_index = 0  # Stores the index where the prefix and suffix hash matched
        power = 1  # Keeps track of powers of the base, needed for calculating the suffix hash
        mod = 10 ** 9 + 7  # A large prime modulus to avoid overflow and collisions in the hash

        # Iterate through each character of the string
        for i, c in enumerate(s):
            char = (ord(c) - ord('a') + 1)  # Map the character to an integer value ('a' -> 1, 'b' -> 2, ..., 'z' -> 26)

            # Update the rolling hash for the prefix (computed in a left-to-right fashion)
            prefix = (prefix * base) % mod  # Shift previous prefix hash by one position (multiply by base)
            prefix = (prefix + char) % mod  # Add the current character's value to the prefix hash

            # Update the rolling hash for the suffix (computed in a right-to-left fashion)
            suffix = (suffix + char * power) % mod  # Add the current character's weighted value to the suffix hash
            power = (power * base) % mod  # Update the power for the next character in the suffix hash calculation

            # If the prefix and suffix hashes are equal, we found a potential palindrome
            if prefix == suffix:
                last_index = i  # Update last_index to the current position as this is the longest palindrome seen so far

        # After the loop, the longest prefix palindrome is identified up to last_index
        # Extract the suffix (part of the string after the palindrome)
        suffix = s[last_index + 1:]

        # Reverse the suffix and prepend it to the original string to form the shortest palindrome
        return suffix[::-1] + s
