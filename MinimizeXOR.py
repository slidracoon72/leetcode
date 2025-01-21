class Solution:
    # Neetcode: https://www.youtube.com/watch?v=xhD78PX8Nss&ab_channel=NeetCodeIO
    # Time: O(logn), Space: O(1)
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Helper function to count the number of set bits (1s) in a binary representation of a number
        def count_bits(n):
            count = 0
            while n > 0:
                count += n & 1  # Check if the least significant bit is 1 and increment count
                n = n >> 1  # Right-shift the number to process the next bit
            return count

        # Count the number of set bits in num1 and num2
        cnt1, cnt2 = count_bits(num1), count_bits(num2)

        # Initialize x with num1, as we will modify it to minimize XOR
        x = num1
        i = 0  # Bit position index

        # Remove Least Significant Bit
        # If num1 has more set bits than num2, reduce the number of set bits in x
        while cnt1 > cnt2:
            # Check if the current bit (1 << i) is set in x
            if x & (1 << i):
                cnt1 -= 1  # Decrease the count of set bits
                x = x ^ (1 << i)  # Toggle the current bit from 1 to 0
            i += 1  # Move to the next bit position

        # Add Least Significant Bit
        # If num2 has more set bits than num1, increase the number of set bits in x
        while cnt2 > cnt1:
            # Check if the current bit (1 << i) is not set in x
            if x & (1 << i) == 0:
                cnt1 += 1  # Increase the count of set bits
                x = x | (1 << i)  # Toggle the current bit from 0 to 1
            i += 1  # Move to the next bit position

        # Return the modified x that has the same number of set bits as num2
        return x


c = Solution()
print(c.minimizeXor(3, 5))
print(c.minimizeXor(1, 12))
print(c.minimizeXor(3, 7))
