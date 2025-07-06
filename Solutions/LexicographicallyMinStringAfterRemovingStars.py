# LC:3170 - Lexicographically Minimum String After Removing Stars

class Solution:
    # Greedy Algorithm
    # Time: O(N), Space: O(N)
    def clearStars(self, s: str) -> str:
        # Create a list of 26 lists to store positions of each character 'a' to 'z'
        count = [[] for _ in range(26)]

        # Convert the string to a list for in-place modification
        list_s = list(s)

        # Iterate through the string
        for i, c in enumerate(s):
            if c != '*':
                # Store the index of each character in its corresponding bucket
                count[ord(c) - ord('a')].append(i)
            else:
                # Find the smallest lexicographical character seen so far
                for i in range(26):
                    if count[i]:
                        # Get the position of the rightmost occurrence of the smallest character
                        pos = count[i][-1]
                        # Mark it as '*' (effectively removing it)
                        list_s[pos] = '*'
                        # Remove the index from the bucket
                        count[i].pop()
                        break

        # Build the final string by removing all '*' characters
        return ''.join([c for c in list_s if c != '*'])


c = Solution()
s = "aaba*"
print(c.clearStars(s))
