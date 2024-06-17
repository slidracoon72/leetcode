from typing import List


class Solution:
    """
       @param: strs: a list of strings
       @return: encodes a list of strings to a single string
    """

    def encode(self, strs: List[str]) -> str:
        res = ""
        # Iterate over each string in the list
        for s in strs:
            # Append the length of the string, a delimiter '#', and the string itself to the result
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: an encoded string
    @return: decodes a single string to a list of strings
    """

    def decode(self, strs: str) -> List[str]:
        res = []  # List to hold the decoded strings
        i = 0  # Pointer to iterate through the encoded string

        while i < len(strs):
            j = i
            # Find the position of the delimiter '#'
            while strs[j] != '#':
                j += 1
            # Extract the length of the next string
            length = int(strs[i:j])
            # Extract the string using the length and the position of '#'
            res.append(strs[j + 1: j + 1 + length])
            # Move the pointer to the start of the next encoded string
            i = j + 1 + length
        return res


c = Solution()
message = ["leet", "co#de"]
print("Initial Message: ", message)
encoded_message = c.encode(message)
print("Encoded Message: ", encoded_message)
decoded_message = c.decode(encoded_message)
print("Decoded Message: ", decoded_message)
