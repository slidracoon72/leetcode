# s = "3[a]2[bc]"
s = "3[a2[c]]"
num_list = []
alpha = ""
ans = ""
flag = False
for i in range(len(s)):
    if s[i].isnumeric():
        num_list.append(s[i])
        # print(num_list)
    if s[i] == '[':
        flag = True
    if s[i].isalpha() and flag:
        alpha += s[i]
    if s[i] == ']':
        if (len(num_list)) > 0:
            p = int(num_list.pop())
            ans += alpha * p
            flag = False
            alpha = ""


# print(num_list)
# print(ans)


class Solution(object):
    def decodeString(self, s):
        stack = []
        curNum = 0
        curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
            elif c.isdigit():  # curNum*10+int(c) is helpful in keep track of more than 1 digit number
                curNum = curNum * 10 + int(c)
            else:
                curString += c
        return curString


c = Solution()
s = "3[a2[c]]"
print(c.decodeString(s))
