from typing import List, Dict, Tuple
import math


class DynamicProgramming:
    """
    Comprehensive collection of Dynamic Programming patterns and solutions.
    Each solution includes time complexity, space complexity, and detailed explanations.
    """
    
    def fibonacci_memoization(self, n: int) -> int:
        """
        Fibonacci using memoization (top-down DP).
        
        Time Complexity: O(n)
        Space Complexity: O(n) for memoization cache
        
        Args:
            n: The nth Fibonacci number to calculate
            
        Returns:
            The nth Fibonacci number
        """
        memo = {}
        
        def fib(n: int) -> int:
            if n in memo:
                return memo[n]
            if n <= 1:
                return n
            
            memo[n] = fib(n - 1) + fib(n - 2)
            return memo[n]
        
        return fib(n)
    
    def fibonacci_tabulation(self, n: int) -> int:
        """
        Fibonacci using tabulation (bottom-up DP).
        
        Time Complexity: O(n)
        Space Complexity: O(1) - only storing last two values
        
        Args:
            n: The nth Fibonacci number to calculate
            
        Returns:
            The nth Fibonacci number
        """
        if n <= 1:
            return n
        
        prev, curr = 0, 1
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr
        
        return curr
    
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        """
        Find the length of the longest common subsequence between two strings.
        
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        
        Args:
            text1: First string
            text2: Second string
            
        Returns:
            Length of the longest common subsequence
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
    
    def longest_increasing_subsequence(self, nums: List[int]) -> int:
        """
        Find the length of the longest strictly increasing subsequence.
        
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        
        Args:
            nums: List of integers
            
        Returns:
            Length of the longest increasing subsequence
        """
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
    def longest_increasing_subsequence_binary_search(self, nums: List[int]) -> int:
        """
        Find the length of the longest strictly increasing subsequence using binary search.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Args:
            nums: List of integers
            
        Returns:
            Length of the longest increasing subsequence
        """
        if not nums:
            return 0
        
        # dp[i] represents the smallest tail value for LIS of length i+1
        dp = []
        
        for num in nums:
            # Binary search to find the position to insert num
            left, right = 0, len(dp)
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            
            if left == len(dp):
                dp.append(num)
            else:
                dp[left] = num
        
        return len(dp)
    
    def coin_change(self, coins: List[int], amount: int) -> int:
        """
        Find the minimum number of coins needed to make up the given amount.
        
        Time Complexity: O(amount * len(coins))
        Space Complexity: O(amount)
        
        Args:
            coins: List of available coin denominations
            amount: Target amount to make
            
        Returns:
            Minimum number of coins needed, or -1 if impossible
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
    
    def coin_change_combinations(self, coins: List[int], amount: int) -> int:
        """
        Find the number of different combinations of coins that make up the given amount.
        
        Time Complexity: O(amount * len(coins))
        Space Complexity: O(amount)
        
        Args:
            coins: List of available coin denominations
            amount: Target amount to make
            
        Returns:
            Number of different combinations
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]
    
    def edit_distance(self, word1: str, word2: str) -> int:
        """
        Find the minimum number of operations (insert, delete, replace) to convert word1 to word2.
        
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        
        Args:
            word1: Source string
            word2: Target string
            
        Returns:
            Minimum number of operations
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
    
    def knapsack_01(self, weights: List[int], values: List[int], capacity: int) -> int:
        """
        0/1 Knapsack problem: Find maximum value that can be achieved with given capacity.
        
        Time Complexity: O(n * capacity)
        Space Complexity: O(capacity)
        
        Args:
            weights: List of item weights
            values: List of item values
            capacity: Maximum weight capacity
            
        Returns:
            Maximum value achievable
        """
        n = len(weights)
        dp = [0] * (capacity + 1)
        
        for i in range(n):
            for w in range(capacity, weights[i] - 1, -1):
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
        
        return dp[capacity]
    
    def house_robber(self, nums: List[int]) -> int:
        """
        House Robber: Find maximum amount that can be robbed without robbing adjacent houses.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            nums: List of house values
            
        Returns:
            Maximum amount that can be robbed
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        prev, curr = 0, nums[0]
        
        for i in range(1, len(nums)):
            prev, curr = curr, max(curr, prev + nums[i])
        
        return curr
    
    def house_robber_circular(self, nums: List[int]) -> int:
        """
        House Robber II: Houses are arranged in a circle.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            nums: List of house values in circular arrangement
            
        Returns:
            Maximum amount that can be robbed
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Rob first house to second-to-last, or second house to last
        return max(self._rob_range(nums, 0, len(nums) - 2),
                  self._rob_range(nums, 1, len(nums) - 1))
    
    def _rob_range(self, nums: List[int], start: int, end: int) -> int:
        """Helper function for circular house robber."""
        if start > end:
            return 0
        
        prev, curr = 0, nums[start]
        
        for i in range(start + 1, end + 1):
            prev, curr = curr, max(curr, prev + nums[i])
        
        return curr
    
    def climb_stairs(self, n: int) -> int:
        """
        Climbing Stairs: Find number of ways to climb n stairs (1 or 2 steps at a time).
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            n: Number of stairs
            
        Returns:
            Number of ways to climb
        """
        if n <= 2:
            return n
        
        prev, curr = 1, 2
        
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr
        
        return curr
    
    def unique_paths(self, m: int, n: int) -> int:
        """
        Unique Paths: Find number of unique paths from top-left to bottom-right.
        
        Time Complexity: O(m * n)
        Space Complexity: O(n)
        
        Args:
            m: Number of rows
            n: Number of columns
            
        Returns:
            Number of unique paths
        """
        dp = [1] * n
        
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        
        return dp[n - 1]
    
    def unique_paths_with_obstacles(self, obstacle_grid: List[List[int]]) -> int:
        """
        Unique Paths II: With obstacles in the grid.
        
        Time Complexity: O(m * n)
        Space Complexity: O(n)
        
        Args:
            obstacle_grid: Grid with obstacles (1 = obstacle, 0 = empty)
            
        Returns:
            Number of unique paths
        """
        if not obstacle_grid or obstacle_grid[0][0] == 1:
            return 0
        
        m, n = len(obstacle_grid), len(obstacle_grid[0])
        dp = [0] * n
        dp[0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacle_grid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        
        return dp[n - 1]
    
    def word_break(self, s: str, word_dict: List[str]) -> bool:
        """
        Word Break: Check if string can be segmented into dictionary words.
        
        Time Complexity: O(n^3) where n is length of string
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
    
    def palindromic_substrings(self, s: str) -> int:
        """
        Count all palindromic substrings in a string.
        
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        
        Args:
            s: Input string
            
        Returns:
            Number of palindromic substrings
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        
        # Single characters are palindromes
        for i in range(n):
            dp[i][i] = True
            count += 1
        
        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1
        
        # Check for palindromes of length > 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1
        
        return count


# Example usage and testing
if __name__ == "__main__":
    dp = DynamicProgramming()
    
    print("Dynamic Programming Demo:")
    print("========================")
    
    # Test Fibonacci
    print(f"Fibonacci(10) with memoization: {dp.fibonacci_memoization(10)}")
    print(f"Fibonacci(10) with tabulation: {dp.fibonacci_tabulation(10)}")
    
    # Test LCS
    print(f"LCS of 'ABCDGH' and 'AEDFHR': {dp.longest_common_subsequence('ABCDGH', 'AEDFHR')}")
    
    # Test LIS
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"LIS of {nums}: {dp.longest_increasing_subsequence(nums)}")
    print(f"LIS (binary search) of {nums}: {dp.longest_increasing_subsequence_binary_search(nums)}")
    
    # Test Coin Change
    coins = [1, 2, 5]
    amount = 11
    print(f"Min coins for amount {amount}: {dp.coin_change(coins, amount)}")
    print(f"Number of combinations for amount {amount}: {dp.coin_change_combinations(coins, amount)}")
    
    # Test Edit Distance
    print(f"Edit distance 'horse' -> 'ros': {dp.edit_distance('horse', 'ros')}")
    
    # Test House Robber
    houses = [2, 7, 9, 3, 1]
    print(f"House robber max: {dp.house_robber(houses)}")
    print(f"House robber circular max: {dp.house_robber_circular(houses)}")
    
    # Test Climbing Stairs
    print(f"Ways to climb 5 stairs: {dp.climb_stairs(5)}")
    
    # Test Unique Paths
    print(f"Unique paths in 3x7 grid: {dp.unique_paths(3, 7)}")
    
    # Test Word Break
    s = "leetcode"
    word_dict = ["leet", "code"]
    print(f"Word break '{s}': {dp.word_break(s, word_dict)}")
    
    # Test Palindromic Substrings
    print(f"Palindromic substrings in 'aaa': {dp.palindromic_substrings('aaa')}") 