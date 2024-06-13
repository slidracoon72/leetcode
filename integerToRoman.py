class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_value_list = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
                             ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]

        result = ""
        for symbol, value in reversed(symbol_value_list):
            if num // value:
                count = num // value
                result += symbol * count
                num = num % value
        return result


class MySolution:
    def intToRoman(self, num: int) -> str:
        # s = "LVIII"
        # s = "III"
        s = "MCMXCIV"
        d = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M", 4: "IV", 9: "IX", 40: "XL", 90: "XC",
             400: "CD",
             900: "CM"}
        # f = {4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}

        # num = str(1994)
        num = str(60)

        l = list()
        size = len(num)
        print(size)
        for i in num:
            x = '0' * (size - 1)
            l.append(i + x)
            size -= 1

        print(l)
        a = list()
        for x in l:
            if int(x) in d:
                a.append(d[int(x)])
        print(a)

        t = "".join(a)
        print(t)

        return t


c = Solution()
print(c.intToRoman(3))
print(c.intToRoman(58))
print(c.intToRoman(1994))
