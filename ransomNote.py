class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ran = dict()
        mag = dict()

        for c in ransomNote:
            if c in ran:
                ran[c] += 1
            else:
                ran[c] = 1

        for c in magazine:
            if c in mag:
                mag[c] += 1
            else:
                mag[c] = 1

        print(ran)
        print(mag)

        b = False
        for k in ran:
            if k in mag and ran[k] <= mag[k]:
                b = True
            else:
                b = False
                break
        return b


ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
c = Solution()
print(c.canConstruct(ransomNote, magazine))
