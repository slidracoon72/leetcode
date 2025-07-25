class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []  # List to store the binary result in reverse
        carry = 0  # Variable to keep track of carry from addition
        i, j = len(a) - 1, len(b) - 1  # Pointers to the end of both strings

        # Loop through both strings from right to left
        while i >= 0 or j >= 0 or carry > 0:
            # Get digit from a if i is valid, else 0
            digitA = int(a[i]) if i >= 0 else 0
            # Get digit from b if j is valid, else 0
            digitB = int(b[j]) if j >= 0 else 0

            # Add the digits along with the carry
            total = digitA + digitB + carry
            # Append the result's least significant bit (0 or 1)
            res.append(total % 2)
            # Update the carry (0 or 1)
            carry = total // 2
            # Move to the next digits
            i, j = i - 1, j - 1

        # Reverse the result list and convert to string
        res = res[::-1]
        return "".join(map(str, res))  # Join list elements to form final binary string

    def addBinary1(self, a: str, b: str) -> str:
        total = int(a, 2) + int(b, 2)
        return bin(total)[2:]


c = Solution()
a = "101"
b = "10"
print(c.addBinary(a, b))
