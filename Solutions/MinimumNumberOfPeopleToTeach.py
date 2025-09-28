# DO AGAIN

class Solution:
    def minimumTeachings(self, n, languages, friendships):
        # convert to sets for easy check
        langs = [set(l) for l in languages]

        # find friendships where users cannot communicate
        bad_pairs = []
        for u, v in friendships:
            u -= 1  # to 0-index
            v -= 1
            if langs[u].isdisjoint(langs[v]):  # no common language
                bad_pairs.append((u, v))

        if not bad_pairs:  # already fine
            return 0

        # try teaching each language and count how many users need it
        ans = float("inf")
        for lang in range(1, n + 1):
            need = set()
            for u, v in bad_pairs:
                if lang not in langs[u]:
                    need.add(u)
                if lang not in langs[v]:
                    need.add(v)
            ans = min(ans, len(need))

        return ans
