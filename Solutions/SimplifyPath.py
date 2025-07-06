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


c = Solution()
path = "/home/user/Documents/../Pictures"
print(c.simplifyPath(path))
