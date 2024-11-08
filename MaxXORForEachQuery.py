from typing import List


class Solution:
    # Time: O(n), Space: O(n)
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # Initialize the variable 'xor' to 0, which will store the XOR of all elements in nums
        xor = 0

        # Perform XOR for all elements in nums
        for n in nums:
            xor ^= n

        # Calculate the maximum possible value for a number with 'maximumBit' bits
        k = 2 ** maximumBit - 1

        # Initialize an empty list to store the result
        answer = []

        # Iterate through the nums list in reverse order
        for n in reversed(nums):
            # Append the XOR of current xor value and k to the answer list
            answer.append(xor ^ k)

            # Update the 'xor' by XOR-ing it with the current element 'n'
            xor ^= n

        # Return the final answer list
        return answer
