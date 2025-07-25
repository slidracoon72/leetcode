class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        if n < 3:
            return False

        vowels = {'a', 'e', 'i', 'o', 'u'}
        vow = False
        conso = False

        for c in word:
            c = c.lower()
            if not c.isalnum():
                return False
            if c in vowels:
                vow = True
            if not c.isdigit() and c not in vowels:
                conso = True

        return conso and vow

    # Similar as above
    def isValid1(self, word: str) -> bool:
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False

        for c in word:
            if c.isalpha():
                if c.lower() in "aeiou":
                    has_vowel = True
                else:
                    has_consonant = True
            elif not c.isdigit():
                return False

        return has_vowel and has_consonant


c = Solution()
word = "234Adas"
print(c.isValid(word))
print(c.isValid1(word))
