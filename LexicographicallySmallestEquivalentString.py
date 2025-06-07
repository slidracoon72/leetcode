from collections import defaultdict


class Solution:
    # Solved using DFS
    # Time: O(N + M), Space: O(N + M)
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Build graph of equivalences
        graph = defaultdict(list)
        for a, b in zip(s1, s2):
            graph[a].append(b)
            graph[b].append(a)

        # Memoization to avoid repeating DFS for same character
        smallest_char_map = {}

        # DFS to find the smallest lex character in the group
        def dfs(char, visited, group_chars):
            visited.add(char)
            group_chars.append(char)
            for neighbor in graph[char]:
                if neighbor not in visited:
                    dfs(neighbor, visited, group_chars)

        # Main processing for each character in baseStr
        result = []
        for ch in baseStr:
            if ch not in graph:
                # No equivalence → keep as is
                result.append(ch)
            elif ch in smallest_char_map:
                # Already computed → use cached result
                result.append(smallest_char_map[ch])
            else:
                # New equivalence group → find all connected chars
                visited = set()
                group_chars = []
                dfs(ch, visited, group_chars)

                # Find the lex smallest and cache result for all in group
                smallest = min(group_chars)
                for c in group_chars:
                    smallest_char_map[c] = smallest
                result.append(smallest)

        return ''.join(result)


c = Solution()
s1 = "parker"
s2 = "morris"
baseStr = "parser"
print(c.smallestEquivalentString(s1, s2, baseStr))
