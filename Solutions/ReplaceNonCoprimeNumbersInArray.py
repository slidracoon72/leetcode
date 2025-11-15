from math import gcd  # Import gcd (Greatest Common Divisor) function
from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        # Stack will hold the current list of processed numbers
        stack = []

        for num in nums:
            # Keep merging with the last element in the stack
            # as long as they are NOT coprime (gcd > 1)
            while stack:
                g = gcd(stack[-1], num)  # Compute gcd of top element and current number
                if g == 1:  # If they are coprime, no merging is needed
                    break

                # Merge the two numbers (replace them with their LCM)
                # LCM(a,b) = (a*b) / gcd(a,b)
                num = (num * stack.pop()) // g

            # After merging, push the resulting number back to stack
            stack.append(num)

        # Final stack contains all numbers after replacing non-coprimes
        return stack


c = Solution()
nums = [6, 4, 3, 2, 7, 6, 2]
print(c.replaceNonCoprimes(nums))
