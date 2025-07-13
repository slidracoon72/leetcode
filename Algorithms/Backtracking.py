from typing import List, Set, Dict, Optional
from collections import Counter


class Backtracking:
    """
    Comprehensive Backtracking implementation with common patterns and templates.
    
    Backtracking is a general algorithm for finding all (or some) solutions to computational problems,
    particularly constraint satisfaction problems. It incrementally builds candidates to the solutions,
    and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly
    be completed to a valid solution.
    
    Common Patterns:
    - Subset/Permutation/Combination generation
    - N-Queens
    - Sudoku solver
    - Word search
    - Path finding
    
    Time Complexity: Usually exponential O(k^n) where k is branching factor, n is depth
    Space Complexity: Usually O(n) for recursion stack
    """
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Subsets (LeetCode 78)
        Generate all possible subsets of a set.
        
        Time Complexity: O(2^n)
        Space Complexity: O(n) for recursion stack
        
        Args:
            nums: Array of integers
            
        Returns:
            List of all possible subsets
        """
        result = []
        
        def backtrack(start: int, current: List[int]):
            result.append(current[:])
            
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
        
        backtrack(0, [])
        return result
    
    def subsets_with_duplicates(self, nums: List[int]) -> List[List[int]]:
        """
        Subsets II (LeetCode 90)
        Generate all possible subsets with duplicates handled.
        
        Time Complexity: O(2^n)
        Space Complexity: O(n)
        
        Args:
            nums: Array of integers (may contain duplicates)
            
        Returns:
            List of all possible subsets
        """
        nums.sort()
        result = []
        
        def backtrack(start: int, current: List[int]):
            result.append(current[:])
            
            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
        
        backtrack(0, [])
        return result
    
    def permutations(self, nums: List[int]) -> List[List[int]]:
        """
        Permutations (LeetCode 46)
        Generate all possible permutations of an array.
        
        Time Complexity: O(n!)
        Space Complexity: O(n)
        
        Args:
            nums: Array of integers
            
        Returns:
            List of all possible permutations
        """
        result = []
        used = [False] * len(nums)
        
        def backtrack(current: List[int]):
            if len(current) == len(nums):
                result.append(current[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current.append(nums[i])
                    backtrack(current)
                    current.pop()
                    used[i] = False
        
        backtrack([])
        return result
    
    def permutations_with_duplicates(self, nums: List[int]) -> List[List[int]]:
        """
        Permutations II (LeetCode 47)
        Generate all possible permutations with duplicates handled.
        
        Time Complexity: O(n!)
        Space Complexity: O(n)
        
        Args:
            nums: Array of integers (may contain duplicates)
            
        Returns:
            List of all possible permutations
        """
        result = []
        nums.sort()
        used = [False] * len(nums)
        
        def backtrack(current: List[int]):
            if len(current) == len(nums):
                result.append(current[:])
                return
            
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue
                
                used[i] = True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                used[i] = False
        
        backtrack([])
        return result
    
    def combinations(self, n: int, k: int) -> List[List[int]]:
        """
        Combinations (LeetCode 77)
        Generate all possible combinations of k numbers from 1 to n.
        
        Time Complexity: O(C(n,k))
        Space Complexity: O(k)
        
        Args:
            n: Upper bound
            k: Size of each combination
            
        Returns:
            List of all possible combinations
        """
        result = []
        
        def backtrack(start: int, current: List[int]):
            if len(current) == k:
                result.append(current[:])
                return
            
            for i in range(start, n + 1):
                current.append(i)
                backtrack(i + 1, current)
                current.pop()
        
        backtrack(1, [])
        return result
    
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Combination Sum (LeetCode 39)
        Find all combinations that sum to target (can reuse elements).
        
        Time Complexity: O(k * 2^t) where k is average length of combination, t is target
        Space Complexity: O(t)
        
        Args:
            candidates: Array of candidates
            target: Target sum
            
        Returns:
            List of combinations that sum to target
        """
        result = []
        
        def backtrack(start: int, current: List[int], current_sum: int):
            if current_sum == target:
                result.append(current[:])
                return
            elif current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, current_sum + candidates[i])
                current.pop()
        
        backtrack(0, [], 0)
        return result
    
    def combination_sum_ii(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Combination Sum II (LeetCode 40)
        Find all combinations that sum to target (cannot reuse elements).
        
        Time Complexity: O(2^n)
        Space Complexity: O(n)
        
        Args:
            candidates: Array of candidates (may contain duplicates)
            target: Target sum
            
        Returns:
            List of combinations that sum to target
        """
        candidates.sort()
        result = []
        
        def backtrack(start: int, current: List[int], current_sum: int):
            if current_sum == target:
                result.append(current[:])
                return
            elif current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                current.append(candidates[i])
                backtrack(i + 1, current, current_sum + candidates[i])
                current.pop()
        
        backtrack(0, [], 0)
        return result
    
    def n_queens(self, n: int) -> List[List[str]]:
        """
        N-Queens (LeetCode 51)
        Place n queens on nxn chessboard so no two queens threaten each other.
        
        Time Complexity: O(n!)
        Space Complexity: O(n^2)
        
        Args:
            n: Size of chessboard
            
        Returns:
            List of valid board configurations
        """
        result = []
        
        def is_safe(board: List[List[str]], row: int, col: int) -> bool:
            # Check column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # Check diagonal (top-left to bottom-right)
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            # Check diagonal (top-right to bottom-left)
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if board[i][j] == 'Q':
                    return False
            
            return True
        
        def backtrack(board: List[List[str]], row: int):
            if row == n:
                result.append([''.join(row) for row in board])
                return
            
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row + 1)
                    board[row][col] = '.'
        
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(board, 0)
        return result
    
    def n_queens_ii(self, n: int) -> int:
        """
        N-Queens II (LeetCode 52)
        Count number of solutions for n-queens problem.
        
        Time Complexity: O(n!)
        Space Complexity: O(n)
        
        Args:
            n: Size of chessboard
            
        Returns:
            Number of valid solutions
        """
        def is_safe(cols: List[int], row: int, col: int) -> bool:
            for i in range(row):
                if cols[i] == col or abs(cols[i] - col) == abs(i - row):
                    return False
            return True
        
        def backtrack(cols: List[int], row: int) -> int:
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                if is_safe(cols, row, col):
                    cols[row] = col
                    count += backtrack(cols, row + 1)
            return count
        
        cols = [-1] * n
        return backtrack(cols, 0)
    
    def sudoku_solver(self, board: List[List[str]]) -> None:
        """
        Sudoku Solver (LeetCode 37)
        Solve Sudoku puzzle in-place.
        
        Time Complexity: O(9^(n^2)) in worst case
        Space Complexity: O(n^2)
        
        Args:
            board: 9x9 Sudoku board
        """
        def is_valid(board: List[List[str]], row: int, col: int, num: str) -> bool:
            # Check row
            for j in range(9):
                if board[row][j] == num:
                    return False
            
            # Check column
            for i in range(9):
                if board[i][col] == num:
                    return False
            
            # Check 3x3 box
            box_row, box_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if board[i][j] == num:
                        return False
            
            return True
        
        def solve() -> bool:
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if is_valid(board, i, j, num):
                                board[i][j] = num
                                if solve():
                                    return True
                                board[i][j] = '.'
                        return False
            return True
        
        solve()
    
    def word_search(self, board: List[List[str]], word: str) -> bool:
        """
        Word Search (LeetCode 79)
        Check if word exists in 2D board by connecting adjacent letters.
        
        Time Complexity: O(m * n * 4^l) where l is word length
        Space Complexity: O(l) for recursion stack
        
        Args:
            board: 2D board of characters
            word: Word to search for
            
        Returns:
            True if word exists, False otherwise
        """
        def backtrack(i: int, j: int, index: int) -> bool:
            if index == len(word):
                return True
            
            if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or 
                board[i][j] != word[index]):
                return False
            
            # Mark as visited
            temp = board[i][j]
            board[i][j] = '#'
            
            # Try all four directions
            result = (backtrack(i + 1, j, index + 1) or
                     backtrack(i - 1, j, index + 1) or
                     backtrack(i, j + 1, index + 1) or
                     backtrack(i, j - 1, index + 1))
            
            # Restore
            board[i][j] = temp
            return result
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        
        return False
    
    def palindrome_partitioning(self, s: str) -> List[List[str]]:
        """
        Palindrome Partitioning (LeetCode 131)
        Partition string into palindromic substrings.
        
        Time Complexity: O(n * 2^n)
        Space Complexity: O(n)
        
        Args:
            s: Input string
            
        Returns:
            List of all palindromic partitions
        """
        def is_palindrome(s: str, left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        result = []
        
        def backtrack(start: int, current: List[str]):
            if start == len(s):
                result.append(current[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s, start, end - 1):
                    current.append(s[start:end])
                    backtrack(end, current)
                    current.pop()
        
        backtrack(0, [])
        return result
    
    def generate_parentheses(self, n: int) -> List[str]:
        """
        Generate Parentheses (LeetCode 22)
        Generate all valid combinations of n pairs of parentheses.
        
        Time Complexity: O(4^n / sqrt(n))
        Space Complexity: O(n)
        
        Args:
            n: Number of pairs of parentheses
            
        Returns:
            List of valid parentheses combinations
        """
        result = []
        
        def backtrack(current: str, open_count: int, close_count: int):
            if len(current) == 2 * n:
                result.append(current)
                return
            
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        backtrack('', 0, 0)
        return result
    
    def letter_combinations(self, digits: str) -> List[str]:
        """
        Letter Combinations of a Phone Number (LeetCode 17)
        Generate all possible letter combinations for phone number.
        
        Time Complexity: O(4^n) where n is number of digits
        Space Complexity: O(n)
        
        Args:
            digits: String of digits
            
        Returns:
            List of all possible letter combinations
        """
        if not digits:
            return []
        
        digit_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index: int, current: str):
            if index == len(digits):
                result.append(current)
                return
            
            for char in digit_map[digits[index]]:
                backtrack(index + 1, current + char)
        
        backtrack(0, '')
        return result
    
    def restore_ip_addresses(self, s: str) -> List[str]:
        """
        Restore IP Addresses (LeetCode 93)
        Restore valid IP addresses from string.
        
        Time Complexity: O(3^4) = O(81)
        Space Complexity: O(1)
        
        Args:
            s: String of digits
            
        Returns:
            List of valid IP addresses
        """
        result = []
        
        def is_valid(segment: str) -> bool:
            if len(segment) > 3 or (len(segment) > 1 and segment[0] == '0'):
                return False
            return 0 <= int(segment) <= 255
        
        def backtrack(start: int, current: List[str]):
            if len(current) == 4:
                if start == len(s):
                    result.append('.'.join(current))
                return
            
            for end in range(start + 1, min(start + 4, len(s) + 1)):
                segment = s[start:end]
                if is_valid(segment):
                    current.append(segment)
                    backtrack(end, current)
                    current.pop()
        
        backtrack(0, [])
        return result


# Example usage and testing
if __name__ == "__main__":
    print("Backtracking Demo:")
    print("==================")
    
    bt = Backtracking()
    
    # Subsets
    nums = [1, 2, 3]
    subsets = bt.subsets(nums)
    print(f"Subsets of {nums}: {subsets}")
    
    # Subsets with duplicates
    nums = [1, 2, 2]
    subsets_dup = bt.subsets_with_duplicates(nums)
    print(f"Subsets of {nums} (with duplicates): {subsets_dup}")
    
    # Permutations
    permutations = bt.permutations(nums)
    print(f"Permutations of {nums}: {permutations}")
    
    # Combinations
    n, k = 4, 2
    combinations = bt.combinations(n, k)
    print(f"Combinations of {k} numbers from 1 to {n}: {combinations}")
    
    # Combination Sum
    candidates = [2, 3, 6, 7]
    target = 7
    combo_sum = bt.combination_sum(candidates, target)
    print(f"Combination sum {target} from {candidates}: {combo_sum}")
    
    # N-Queens
    n = 4
    queens = bt.n_queens(n)
    print(f"N-Queens solutions for n={n}: {len(queens)} solutions")
    for i, solution in enumerate(queens[:2]):  # Show first 2 solutions
        print(f"Solution {i+1}:")
        for row in solution:
            print(f"  {row}")
    
    # Generate Parentheses
    n = 3
    parentheses = bt.generate_parentheses(n)
    print(f"Valid parentheses for n={n}: {parentheses}")
    
    # Letter Combinations
    digits = "23"
    letter_combo = bt.letter_combinations(digits)
    print(f"Letter combinations for '{digits}': {letter_combo}")
    
    # Palindrome Partitioning
    s = "aab"
    palin_part = bt.palindrome_partitioning(s)
    print(f"Palindrome partitioning of '{s}': {palin_part}")
    
    # Restore IP Addresses
    s = "25525511135"
    ip_addresses = bt.restore_ip_addresses(s)
    print(f"Valid IP addresses for '{s}': {ip_addresses}")
    
    # Word Search
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word = "ABCCED"
    word_exists = bt.word_search(board, word)
    print(f"Word '{word}' exists in board: {word_exists}")
    
    # Sudoku Solver
    sudoku_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print("Solving Sudoku:")
    bt.sudoku_solver(sudoku_board)
    for row in sudoku_board:
        print(f"  {row}") 