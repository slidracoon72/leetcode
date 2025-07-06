# Reverse Strings With Vowels At Start And End
def solution(text):
    vowels = set('aeiouAEIOU')

    def rev_mid(word):
        if len(word) > 2 and word[0] in vowels and word[-1] in vowels:
            return word[0] + word[1:-1][::-1] + word[-1]
        return word

    return [rev_mid(word) for word in text]
