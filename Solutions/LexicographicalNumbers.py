from typing import List


class Solution:
    # Time: O(nlogn), Space: O(n)
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        for i in range(1, n + 1):
            res.append(str(i))
        return map(int, sorted(res))

    # Neetcode: https://www.youtube.com/watch?v=QihtII-FvLo
    # DFS - Recursion
    def lexicalOrder1(self, n: int) -> List[int]:
        res = []

        def dfs(cur):
            if cur > n:
                return
            res.append(cur)

            # call DFS on descendants
            cur = cur * 10
            for i in range(10):
                dfs(cur + i)

        for i in range(1, 10):
            dfs(i)

        return res

    # DFS - Iterative
    # Time: O(n), Space: O(n)
    def lexicalOrder2(self, n: int) -> List[int]:
        res = []  # List to store the result in lexicographical order
        cur = 1  # Start with the smallest lexicographical number (1)

        # Continue until we've added 'n' numbers to the result list
        while len(res) < n:
            res.append(cur)  # Add the current number to the result list

            # Try to go deeper in lexicographical order (i.e., move to the next level by multiplying by 10)
            if cur * 10 <= n:
                cur = cur * 10  # Move down to the next lexicographical number (next child)
            else:
                # If we can't go deeper, we need to backtrack (pop back)
                # Continue backtracking while:
                # - The current number is equal to 'n' (can't go beyond 'n')
                # - OR the last digit of the current number is 9 (no further numbers at this level)
                # eg. if we reach 1999, then 1999->199->19->1, then 1+1=2. now start 2 series
                while cur == n or cur % 10 == 9:
                    cur = cur // 10  # Move back to the previous level by dividing by 10

                cur += 1  # Move to the next sibling in the lexicographical tree

        return res  # Return the final result list containing numbers in lexicographical order


c = Solution()
print(c.lexicalOrder2(136))
