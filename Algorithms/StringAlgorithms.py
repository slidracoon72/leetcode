from typing import List, Optional, Tuple
import hashlib


class StringAlgorithms:
    """
    Comprehensive String Algorithms implementation with common patterns and applications.
    
    String algorithms are fundamental in computer science and are frequently tested
    in coding interviews. This implementation includes:
    - Pattern matching algorithms
    - Palindrome algorithms
    - String manipulation
    - Compression algorithms
    
    Time Complexity: Varies by algorithm
    Space Complexity: Usually O(n) where n is string length
    """
    
    def kmp_search(self, text: str, pattern: str) -> List[int]:
        """
        Knuth-Morris-Pratt (KMP) algorithm for pattern matching.
        
        Time Complexity: O(n + m) where n is text length, m is pattern length
        Space Complexity: O(m)
        
        Args:
            text: Text to search in
            pattern: Pattern to search for
            
        Returns:
            List of starting indices where pattern is found
        """
        if not pattern or not text:
            return []
        
        # Build failure function (longest proper prefix that is also suffix)
        def build_lps(pattern: str) -> List[int]:
            lps = [0] * len(pattern)
            length = 0
            i = 1
            
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            
            return lps
        
        lps = build_lps(pattern)
        result = []
        
        i = j = 0  # i for text, j for pattern
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            
            if j == len(pattern):
                result.append(i - j)
                j = lps[j - 1]
            elif i < len(text) and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return result
    
    def rabin_karp_search(self, text: str, pattern: str, base: int = 256, prime: int = 101) -> List[int]:
        """
        Rabin-Karp algorithm for pattern matching using rolling hash.
        
        Time Complexity: O(n + m) average case, O(nm) worst case
        Space Complexity: O(1)
        
        Args:
            text: Text to search in
            pattern: Pattern to search for
            base: Base for hash function
            prime: Prime number for modulo
            
        Returns:
            List of starting indices where pattern is found
        """
        if not pattern or not text or len(pattern) > len(text):
            return []
        
        n, m = len(text), len(pattern)
        pattern_hash = 0
        text_hash = 0
        h = 1
        result = []
        
        # Calculate h = base^(m-1) % prime
        for i in range(m - 1):
            h = (h * base) % prime
        
        # Calculate hash for pattern and first window of text
        for i in range(m):
            pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
            text_hash = (base * text_hash + ord(text[i])) % prime
        
        # Slide the pattern over text one by one
        for i in range(n - m + 1):
            if pattern_hash == text_hash:
                # Check if pattern matches at current position
                if text[i:i + m] == pattern:
                    result.append(i)
            
            # Calculate hash for next window
            if i < n - m:
                text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
                if text_hash < 0:
                    text_hash += prime
        
        return result
    
    def manacher_algorithm(self, s: str) -> str:
        """
        Manacher's algorithm to find longest palindromic substring.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            s: Input string
            
        Returns:
            Longest palindromic substring
        """
        if not s:
            return ""
        
        # Transform string to handle even-length palindromes
        transformed = '#' + '#'.join(s) + '#'
        n = len(transformed)
        
        # Array to store palindrome radii
        p = [0] * n
        
        center = right = 0
        
        for i in range(n):
            # Mirror position
            mirror = 2 * center - i
            
            if i < right:
                p[i] = min(right - i, p[mirror])
            
            # Expand palindrome centered at i
            left = i - (p[i] + 1)
            right_expand = i + (p[i] + 1)
            
            while left >= 0 and right_expand < n and transformed[left] == transformed[right_expand]:
                p[i] += 1
                left -= 1
                right_expand += 1
            
            # Update center and right boundary
            if i + p[i] > right:
                center = i
                right = i + p[i]
        
        # Find longest palindrome
        max_len = max(p)
        center_index = p.index(max_len)
        
        # Convert back to original string indices
        start = (center_index - max_len) // 2
        end = start + max_len
        
        return s[start:end]
    
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        """
        Find length of longest common subsequence between two strings.
        
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        
        Args:
            text1: First string
            text2: Second string
            
        Returns:
            Length of longest common subsequence
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]
    
    def longest_common_substring(self, text1: str, text2: str) -> str:
        """
        Find longest common substring between two strings.
        
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        
        Args:
            text1: First string
            text2: Second string
            
        Returns:
            Longest common substring
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        max_len = 0
        end_pos = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        end_pos = i
        
        return text1[end_pos - max_len:end_pos]
    
    def edit_distance(self, word1: str, word2: str) -> int:
        """
        Calculate minimum edit distance (Levenshtein distance) between two strings.
        
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        
        Args:
            word1: First string
            word2: Second string
            
        Returns:
            Minimum number of operations (insert, delete, replace)
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize first row and column
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],      # delete
                                     dp[i][j - 1],      # insert
                                     dp[i - 1][j - 1])  # replace
        
        return dp[m][n]
    
    def is_anagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are anagrams.
        
        Time Complexity: O(n)
        Space Complexity: O(k) where k is character set size
        
        Args:
            s: First string
            t: Second string
            
        Returns:
            True if anagrams, False otherwise
        """
        if len(s) != len(t):
            return False
        
        char_count = {}
        
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        for char in t:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1
        
        return True
    
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group strings by anagrams.
        
        Time Complexity: O(n * k * log k) where n is number of strings, k is max string length
        Space Complexity: O(n * k)
        
        Args:
            strs: List of strings
            
        Returns:
            List of anagram groups
        """
        anagram_groups = {}
        
        for s in strs:
            # Sort characters to create key
            key = ''.join(sorted(s))
            if key not in anagram_groups:
                anagram_groups[key] = []
            anagram_groups[key].append(s)
        
        return list(anagram_groups.values())
    
    def longest_substring_without_repeating(self, s: str) -> int:
        """
        Find length of longest substring without repeating characters.
        
        Time Complexity: O(n)
        Space Complexity: O(min(m, n)) where m is character set size
        
        Args:
            s: Input string
            
        Returns:
            Length of longest substring without repeating characters
        """
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    def minimum_window_substring(self, s: str, t: str) -> str:
        """
        Find minimum window in s that contains all characters in t.
        
        Time Complexity: O(n)
        Space Complexity: O(k) where k is character set size
        
        Args:
            s: Source string
            t: Target string
            
        Returns:
            Minimum window substring
        """
        if not s or not t:
            return ""
        
        # Count characters in t
        target_count = {}
        for char in t:
            target_count[char] = target_count.get(char, 0) + 1
        
        required = len(target_count)
        formed = 0
        window_count = {}
        
        left = right = 0
        min_len = float('inf')
        min_start = 0
        
        while right < len(s):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1
            
            # Try to minimize window
            while left <= right and formed == required:
                char = s[left]
                
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                
                window_count[char] -= 1
                if char in target_count and window_count[char] < target_count[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return s[min_start:min_start + min_len] if min_len != float('inf') else ""
    
    def word_break(self, s: str, word_dict: List[str]) -> bool:
        """
        Check if string can be segmented into dictionary words.
        
        Time Complexity: O(n^3)
        Space Complexity: O(n)
        
        Args:
            s: Input string
            word_dict: List of valid words
            
        Returns:
            True if string can be broken, False otherwise
        """
        word_set = set(word_dict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]
    
    def run_length_encoding(self, s: str) -> str:
        """
        Compress string using run-length encoding.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            s: Input string
            
        Returns:
            Compressed string
        """
        if not s:
            return ""
        
        result = []
        count = 1
        current_char = s[0]
        
        for i in range(1, len(s)):
            if s[i] == current_char:
                count += 1
            else:
                result.append(current_char + str(count))
                current_char = s[i]
                count = 1
        
        result.append(current_char + str(count))
        return ''.join(result)
    
    def run_length_decoding(self, s: str) -> str:
        """
        Decompress string using run-length decoding.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            s: Compressed string
            
        Returns:
            Decompressed string
        """
        if not s:
            return ""
        
        result = []
        i = 0
        
        while i < len(s):
            char = s[i]
            i += 1
            
            # Extract count
            count = ""
            while i < len(s) and s[i].isdigit():
                count += s[i]
                i += 1
            
            # Repeat character
            result.append(char * int(count))
        
        return ''.join(result)
    
    def z_algorithm(self, s: str) -> List[int]:
        """
        Z-algorithm to find all occurrences of pattern in text.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            s: Input string
            
        Returns:
            Z-array where Z[i] is length of longest substring starting at i
        """
        n = len(s)
        z = [0] * n
        
        left = right = 0
        
        for i in range(1, n):
            if i > right:
                # Expand from i
                left = right = i
                while right < n and s[right - left] == s[right]:
                    right += 1
                z[i] = right - left
                right -= 1
            else:
                # Use previously computed values
                k = i - left
                if z[k] < right - i + 1:
                    z[i] = z[k]
                else:
                    left = i
                    while right < n and s[right - left] == s[right]:
                        right += 1
                    z[i] = right - left
                    right -= 1
        
        return z


# Example usage and testing
if __name__ == "__main__":
    print("String Algorithms Demo:")
    print("======================")
    
    sa = StringAlgorithms()
    
    # KMP Search
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    kmp_matches = sa.kmp_search(text, pattern)
    print(f"KMP search for '{pattern}' in '{text}': {kmp_matches}")
    
    # Rabin-Karp Search
    rabin_matches = sa.rabin_karp_search(text, pattern)
    print(f"Rabin-Karp search for '{pattern}' in '{text}': {rabin_matches}")
    
    # Manacher's Algorithm
    s = "babad"
    longest_palindrome = sa.manacher_algorithm(s)
    print(f"Longest palindromic substring in '{s}': '{longest_palindrome}'")
    
    # Longest Common Subsequence
    text1, text2 = "ABCDGH", "AEDFHR"
    lcs_length = sa.longest_common_subsequence(text1, text2)
    print(f"LCS length of '{text1}' and '{text2}': {lcs_length}")
    
    # Longest Common Substring
    lcs_string = sa.longest_common_substring(text1, text2)
    print(f"Longest common substring: '{lcs_string}'")
    
    # Edit Distance
    word1, word2 = "horse", "ros"
    edit_dist = sa.edit_distance(word1, word2)
    print(f"Edit distance between '{word1}' and '{word2}': {edit_dist}")
    
    # Anagram Check
    s1, s2 = "anagram", "nagaram"
    is_anagram = sa.is_anagram(s1, s2)
    print(f"'{s1}' and '{s2}' are anagrams: {is_anagram}")
    
    # Group Anagrams
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    anagram_groups = sa.group_anagrams(strs)
    print(f"Anagram groups: {anagram_groups}")
    
    # Longest Substring Without Repeating
    s = "abcabcbb"
    max_length = sa.longest_substring_without_repeating(s)
    print(f"Longest substring without repeating in '{s}': {max_length}")
    
    # Minimum Window Substring
    s, t = "ADOBECODEBANC", "ABC"
    min_window = sa.minimum_window_substring(s, t)
    print(f"Minimum window of '{t}' in '{s}': '{min_window}'")
    
    # Word Break
    s = "leetcode"
    word_dict = ["leet", "code"]
    can_break = sa.word_break(s, word_dict)
    print(f"Can break '{s}' into words: {can_break}")
    
    # Run Length Encoding
    s = "AAAABBBCCDAA"
    encoded = sa.run_length_encoding(s)
    print(f"Run-length encoding of '{s}': '{encoded}'")
    
    decoded = sa.run_length_decoding(encoded)
    print(f"Run-length decoding: '{decoded}'")
    
    # Z Algorithm
    s = "AABAACAADAABAABA"
    z_array = sa.z_algorithm(s)
    print(f"Z-array for '{s}': {z_array}")
    
    # Performance comparison
    print("\n" + "="*50)
    print("Performance Comparison:")
    print("="*50)
    
    import time
    
    # Test with large strings
    text = "A" * 10000 + "B" * 10000
    pattern = "A" * 100 + "B" * 100
    
    # Time KMP
    start = time.time()
    kmp_result = sa.kmp_search(text, pattern)
    kmp_time = time.time() - start
    
    # Time Rabin-Karp
    start = time.time()
    rabin_result = sa.rabin_karp_search(text, pattern)
    rabin_time = time.time() - start
    
    print(f"KMP time: {kmp_time:.4f}s")
    print(f"Rabin-Karp time: {rabin_time:.4f}s")
    print(f"KMP speedup: {rabin_time/kmp_time:.2f}x")
    
    # Test palindrome algorithms
    s = "A" * 1000 + "B" + "A" * 1000
    
    start = time.time()
    manacher_result = sa.manacher_algorithm(s)
    manacher_time = time.time() - start
    
    print(f"Manacher's algorithm time: {manacher_time:.4f}s")
    print(f"Longest palindrome length: {len(manacher_result)}") 