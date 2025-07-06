class Solution:
    def reverseBits(self, n: int) -> int:
        res = [0] * 32
        for i in range(32):
            res[i] = n % 2
            n = n >> 1

        result_int = int("".join(map(str, res)), 2)
        return result_int

    # Optimal Solution
    # Time Complexity: O(32) = O(1), as the loop runs a fixed number of times (32 bits).
    # Space Complexity: O(1), as no extra data structures are used.
    def reverseBits1(self, n: int) -> int:
        res = 0  # Initialize the result to 0, which will hold the reversed bits.

        # Iterate through all 32 bits of the integer.
        for i in range(32):
            # Extract the i-th bit from the input integer `n`.
            # Right shift `n` by `i` bits and apply a bitwise AND with 1 to isolate the bit.
            bit = (n >> i) & 1

            # Set this extracted bit in the reversed position in the result.
            # Left shift the bit by `(31 - i)` to place it in its reversed position.
            res = res | (bit << (31 - i))

        # Return the integer with bits reversed.
        return res


c = Solution()
n = 0b00000010100101000001111010011100
print(c.reverseBits1(n))
