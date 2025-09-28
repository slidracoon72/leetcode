# DO AGAIN

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []

        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        numerator, denominator = abs(numerator), abs(denominator)

        # Integer part
        res.append(str(numerator // denominator))
        remainder = numerator % denominator

        if remainder == 0:
            return "".join(res)

        res.append(".")

        # Dictionary to store remainder -> index in result
        remainder_map = {}

        while remainder != 0:
            if remainder in remainder_map:
                # Found repeating remainder -> insert '(' at stored index and append ')'
                idx = remainder_map[remainder]
                res.insert(idx, "(")
                res.append(")")
                break

            remainder_map[remainder] = len(res)

            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(res)
