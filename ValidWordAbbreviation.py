class Solution:
    # Time: O(n), Space: O(1)hykkopftgopdr4stiur
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(abbr) and j < len(word):
            if abbr[i] == word[j]:
                i += 1
                j += 1
            elif abbr[i].isdigit():
                if abbr[i] == '0':  # Handle leading zeros
                    return False
                num = ""
                while i < len(abbr) and abbr[i].isdigit():
                    num += abbr[i]
                    i += 1
                j += int(num)
            else:
                return False

        return i == len(abbr) and j == len(word)
