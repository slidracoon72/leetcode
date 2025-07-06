class Solution:
    def compressedString(self, word: str) -> str:
        # Initialize an empty string to store the compressed result
        comp = ""

        # Initialize two pointers, 'i' for the start of the sequence and 'j' to iterate through the string
        i, j = 0, 0

        # Iterate through the string until 'j' reaches the end
        while j < len(word):
            # Store the current character from position 'i'
            cur = word[i]

            # Count how many consecutive characters are the same
            while j < len(word) and cur == word[j]:
                j += 1
                # If the sequence length reaches 9, add the compressed form and reset 'i' to 'j'
                if (j - i) == 9:
                    comp += str(j - i) + cur  # Append the count and character
                    break  # Exit the inner loop to process the next sequence

            # If the loop ends normally (not by break), append the compressed form of the sequence
            else:
                comp += str(j - i) + cur  # Append the count and character

            # Reset 'i' to 'j' to process the next sequence of characters
            i = j

        # Return the final compressed string
        return comp

    def compressedString1(self, word: str) -> str:
        comp = ""
        i, j = 0, 0
        while j < len(word):
            cur = word[i]
            while j < len(word) and cur == word[j]:
                j += 1
            if (j - i) >= 9:
                res = []
                num = j - i
                while num > 0:
                    if num >= 9:
                        res.append(9)
                        num -= 9
                    else:
                        res.append(num)
                        break
                for x in res:
                    comp += str(x) + cur
            else:
                comp += str(j - i) + cur
            i = j
        return comp


c = Solution()
print(c.compressedString("aaaaaaaaaaaaaabbcccccddddffffrrddd"))
