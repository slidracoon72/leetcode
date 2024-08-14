# User Friendly Password System - HackerRank Question
# Tik-Tok Coding Interview Question
class Solution:
    def authEvents(self, events):
        P, M = 131, 10 ** 9 + 7

        def hash(s):
            n = len(s)
            res = 0
            for c in s:
                temp = ord(c) * (P ** (n - 1))
                n -= 1
                res += temp % M
            return res % M

        # Initialize variables
        current_password = ""
        current_hash = -1
        extended_hashes = set()

        # List to store results
        results = []

        for event, param in events:
            if event == 'setPassword':
                # Update the current password and its hash
                current_password = param
                current_hash = hash(current_password)

                # Compute and store all possible hashes of the current password with one additional character
                extended_hashes = set()
                for c in range(ord('a'), ord('z') + 1):
                    extended_hashes.add(hash(current_password + chr(c)))
                for c in range(ord('A'), ord('Z') + 1):
                    extended_hashes.add(hash(current_password + chr(c)))
                for c in range(ord('0'), ord('9') + 1):
                    extended_hashes.add(hash(current_password + chr(c)))

            elif event == 'authorize':
                # Check if the given hash is the current hash or one of the extended hashes
                auth_hash = int(param)
                if auth_hash == current_hash or auth_hash in extended_hashes:
                    results.append(1)
                else:
                    results.append(0)

        return results


events = [["setPassword", "000A"],
          ["authorize", "108738450"],
          ["authorize", "108738449"],
          ["authorize", "244736787"]]

c = Solution()
print(c.authEvents(events))
