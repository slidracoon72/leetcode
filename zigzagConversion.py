s = "PAYPALISHIRING"
numRows = 3

flag = True
i = 0
res = {}
while i != len(s):
    if flag:
        new = s[i:numRows + i]
        print(new)
        index = i
        for x in new:
            res[index] = x
            index += numRows + 1
        flag = False
        i += len(new)
    else:
        new = s[i:(numRows + i) - 2]
        print(new)
        index = i
        for x in new:
            res[index] = x
            index += 2
        flag = True
        i += numRows - 2
print(res)
print(res)
