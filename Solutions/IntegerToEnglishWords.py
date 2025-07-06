# Neetcode: https://www.youtube.com/watch?v=SCtIlKd3mDM
# Time: O(log(num)), Space: O(1)
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        ones_map = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
                    6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
                    11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
                    15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
                    19: 'Nineteen'}

        tens_map = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
                    60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}

        # Takes 3 digits at a time and returns string
        def get_string(n):
            res = []

            hundreds = n // 100
            if hundreds:
                res.append(ones_map[hundreds] + " Hundred")

            last_2 = n % 100
            if last_2 >= 20:
                tens, ones = last_2 // 10, last_2 % 10
                res.append(tens_map[tens * 10])
                if ones:  # if ones is not '0'
                    res.append(ones_map[ones])
            elif last_2:  # If last_2 is not '00' and between 1-19, directly add to res
                res.append(ones_map[last_2])

            return " ".join(res)

        postfix = ["", " Thousand", " Million", " Billion"]
        i = 0
        res = []
        while num:
            # To get last 3 digits
            digits = num % 1000
            s = get_string(digits)
            if s:
                res.append(s + postfix[i])
            # To remove last 3 digits
            num = num // 1000
            i += 1

        # Since larger units are added last, we reverse the list as we want them first
        res.reverse()
        # Convert list to string
        return " ".join(res)


c = Solution()
print(c.numberToWords(321359))
print(c.numberToWords(0))
print(c.numberToWords(786))
print(c.numberToWords(891209932446))
