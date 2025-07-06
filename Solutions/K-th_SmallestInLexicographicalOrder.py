# LC - Hard
# DO AGAIN

class Solution:
    # Passes 40/69 test cases
    # Getting TLE
    # DFS Iterative Approach
    def findKthNumber(self, n: int, k: int) -> int:
        res = 0
        cur = 1
        i = 0
        while i < k:
            res = cur
            if cur * 10 <= n:
                cur = cur * 10
            else:
                while cur == n or cur % 10 == 9:
                    cur = cur // 10
                cur += 1
            i += 1
        return res

    # Neetcode: https://www.youtube.com/watch?v=wRubz1zhVqk
    # Time: O(logn), Space: O(1)
    def findKthNumber1(self, n: int, k: int) -> int:
        cur = 1  # Start with the smallest lexicographical number (1)
        i = 1  # i keeps track of the current position in lexicographical order

        # Function to count how many numbers exist starting with the prefix 'cur'
        def count(cur):
            res = 0  # Count of numbers starting with the prefix 'cur'
            nei = cur + 1  # The next prefix to consider (cur + 1)

            # Calculate the count of numbers with the current prefix 'cur' across levels
            while cur <= n:  # While the prefix 'cur' is valid (within the range)
                # Add the numbers between 'cur' and 'nei', but do not exceed 'n'
                res += min(nei, n + 1) - cur
                # Move to the next level by multiplying 'cur' and 'nei' by 10
                cur *= 10
                nei *= 10
            return res  # Return the total count of numbers starting with 'cur'

        # Iterate until we find the k-th number
        while i < k:
            steps = count(cur)  # Calculate how many numbers exist under the current prefix 'cur'

            # If the k-th number is not under this prefix (i + steps <= k), skip this subtree
            if i + steps <= k:
                cur = cur + 1  # Move to the next prefix (next sibling in lexicographical order)
                i += steps  # Increment 'i' by the number of numbers skipped
            else:
                # If the k-th number is within this subtree, move deeper (to the next level)
                cur *= 10  # Move down to the next level in the lexicographical tree
                i += 1  # Increment 'i' as we're exploring the next number

        # After the loop, 'cur' will be the k-th lexicographical number
        return cur


c = Solution()
print(c.findKthNumber1(13, 2))
print(c.findKthNumber1(1361, 400))
