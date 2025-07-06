# LC - 1432: Max Difference You Can Get From Changing an Integer

class Solution:
    # Greedy Solution
    # Time: O(n), Space: O(1)
    def maxDiff(self, num: int) -> int:
        # Approach:
        # 1. Convert num to string for digit manipulation.
        # 2. For 'a': Replace first non-9 digit with 9.
        # 3. For 'b': If first digit != 1, replace with 1; else, replace first non-0
        #    digit after pos 0 which is not equal to the first digit with 0.
        #    We do this as we can't replace 1 in the first digit with a 0 as the number can't start with a zero.
        # 4. Return int(a) - int(b).

        a = str(num)  # Max number
        b = str(num)  # Min number
        n = len(a)

        # Maximize 'a': Replace first non-9 digit with 9
        pos = 0
        while pos < n and a[pos] == '9':
            pos += 1
        if pos < n:
            a = a.replace(a[pos], '9')

        # Minimize 'b': Use provided logic
        for i, digit in enumerate(b):
            if i == 0:
                if digit != '1':
                    b = b.replace(digit, '1')
                    break
            else:
                # if digit not in [0, 1]:
                if digit != '0' and digit != b[0]:  # b[0] is always 1
                    b = b.replace(digit, '0')
                    break

        # Return difference
        return int(a) - int(b)


c = Solution()
print(c.maxDiff(555))
print(c.maxDiff(9))
