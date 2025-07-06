from typing import List


class Solution:
    # Getting TLE
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for l, r in queries:
            a = 0
            for x in arr[l:r + 1]:
                a = a ^ x
            res.append(a)
        return res

    # Neetcode: https://www.youtube.com/watch?v=1Q4lxfSlbPs
    # Time Complexity: O(m + n), Space: O(m) where m is the length of the `arr` and n is the number of `queries`
    def xorQueries1(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Create a prefix XOR array where prefix[i] will store the XOR of all elements from arr[0] to arr[i-1]
        # The 0th index is initialized to 0 to simplify calculations (acts as a base)
        prefix = [0]

        # Build the prefix XOR array by XORing each element with the cumulative XOR up to that point
        for n in arr:
            # The next value in the prefix is the XOR of the last value in the prefix and the current element
            prefix.append(prefix[-1] ^ n)

        # Initialize the result array to store the XOR result for each query
        res = []

        # Process each query in the format [l, r]
        for l, r in queries:
            # The result of XOR for the range [l, r] can be computed as:
            # prefix[r+1] ^ prefix[l], this effectively cancels out the elements before 'l'
            # An element XOR'd with itself gives 0 (cancels out)
            res.append(prefix[l] ^ prefix[r + 1])

        # Return the result array containing XOR results for each query
        return res


c = Solution()
arr = [1, 3, 4, 8]
queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
print(c.xorQueries1(arr, queries))
