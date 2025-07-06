class Solution:
    # Time: O(high - low), Space: O(1)
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0  # Initialize counter for symmetric integers

        # Iterate over each number in the given range [low, high]
        for i in range(low, high + 1):
            # Convert the number to a list of digits
            i = [int(x) for x in str(i)]

            # Skip numbers with an odd number of digits, as they can't be symmetric
            if len(i) % 2 == 1:
                continue

            n = len(i) // 2  # Midpoint of the digit list

            total = sum(i)  # Total sum of all digits
            first = sum(i[:n])  # Sum of the first half of digits

            # If the sum of the first half equals the sum of the second half,
            # the number is symmetric
            if total == 2 * first:
                res += 1  # Increment the result counter

        return res  # Return the final count of symmetric integers

    def countSymmetricIntegers1(self, low: int, high: int) -> int:
        res = 0
        for a in range(low, high + 1):
            if a < 100 and a % 11 == 0:
                res += 1
            if 1000 <= a < 10000:  # if len(a) == 4 (max value of 'a' is 9999 - given in constraints)
                left = (a // 1000) + (a % 1000 // 100)  # get 1000's place and hundreds place and add
                right = (a % 100 // 10) + (a % 10)  # get tens place and digits place and add
                if left == right:
                    res += 1
        return res


c = Solution()
low = 1
high = 100
print(c.countSymmetricIntegers(low, high))
print(c.countSymmetricIntegers1(low, high))
