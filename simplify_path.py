class Solution:
    # Neetcode Solution
    # Space and Time: O(n)
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ''

        for c in path + '/':
            if c == '/':
                if cur == '..':
                    if stack:
                        stack.pop()
                elif cur != '' and cur != '.':
                    stack.append(cur)
                cur = ''
            else:
                cur += c

        return '/' + '/'.join(stack)

    def simplifyPathMyWay(self, path: str) -> str:
        s = ['/']
        for x in path:
            c = s[-1]
            if (c == '/' and x == c) or (c == '.' and x == c) or x == '.':
                continue
            s.append(x)

        if len(s) == 1:
            return ''.join(s)
        elif s[-1] == '/':
            return ''.join(s[:len(s) - 1])
