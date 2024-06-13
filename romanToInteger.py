# s = "LVIII"
# s = "III"
s = "MCMXCIV"


def romanToInt1(s: str) -> int:
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    f = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

    preNode = None
    Node = None
    solution = 0

    for i in range(0, len(s)):
        if i != 0:
            preNode = s[i - 1]

        Node = s[i]
        if preNode != None:
            if (preNode == "I" and Node == "V") or (preNode == "I" and Node == "X") or (
                    preNode == "X" and Node == "L") or (
                    preNode == "X" and Node == "C") or (preNode == "C" and Node == "D") or (
                    preNode == "C" and Node == "M"):
                solution = solution - d[preNode] + (f[preNode + Node])
            else:
                solution += d[Node]
        else:
            solution += d[Node]

    return solution


def romanToInt2(s: str) -> int:
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    e = ["IV", "IX", "XL", "XC", "CD", "CM"]
    f = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

    test = []
    for i in e:
        if i in s:
            test.append(f[i])

    n = []
    for i in range(len(s)):
        if s[i:i + 2] in e:
            n.append(s[i:i + 2])

    t = "".join(n)

    l1 = []
    l2 = []
    for i in s:
        l1.append(i)
    for i in t:
        l2.append(i)

    sum1, sum2 = 0, 0

    for i in l1:
        sum1 += d[i]

    for j in l2:
        sum2 += d[j]

    diff = sum1 - sum2
    sol = sum(test) + diff
    return sol


print("Vedanshu:", romanToInt1(s))
print("Rahul:", romanToInt2(s))
