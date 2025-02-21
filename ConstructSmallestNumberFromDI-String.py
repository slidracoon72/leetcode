# LC-2375: Construct Smallest Number From DI String

# Solved using stack
# Neetcode: https://www.youtube.com/watch?v=GgN8d22BEf0&ab_channel=NeetCodeIO
# Time: O(n), Space: O(n)
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """
        Generates the smallest lexicographical number following the given pattern of 'I' (increasing)
        and 'D' (decreasing).

        :param pattern: A string consisting of 'I' and 'D' representing the sequence constraints.
        :return: The smallest possible number that follows the pattern.
        """
        res, stack = [], []  # 'res' stores the final result, 'stack' helps manage decreasing sequences.

        for i in range(len(pattern) + 1):
            stack.append(i + 1)  # Push the next number onto the stack.

            # When the end is reached or an 'I' (increase) is encountered, pop all elements from the stack
            if i == len(pattern) or pattern[i] == "I":
                while stack:
                    res.append(str(stack.pop()))  # Append popped values to 'res' in reverse order

        return "".join(res)  # Convert the result list into a string and return.


c = Solution()
pattern = "IIIDIDDD"
print(c.smallestNumber(pattern))
