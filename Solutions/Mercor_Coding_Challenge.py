from collections import defaultdict
from typing import Iterable


class ReferralError(ValueError):
    pass


class ReferralNetwork:
    def __init__(self) -> None:
        self.parent = {}
        self.children = defaultdict(set)
        self.nodes = set()

    def add_referral(self, referrer: str, candidate: str) -> None:
        if referrer == candidate:
            raise ReferralError("You cant do self referral")

        if candidate in self.parent:
            raise ReferralError("Candidate has a referral already")

        if self.cycle(candidate, referrer):
            raise ReferralError("This edge creates a cycle")

        self.children[referrer].add(candidate)
        self.parent[candidate] = referrer
        self.nodes.add(referrer)
        self.nodes.add(candidate)

        if candidate not in self.children:
            self.children[candidate] = set()

    def cycle(self, start: str, target: str) -> bool:
        if start == target:
            return True

        stack = [start]
        seen = set()

        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)

            for nei in self.children.get(node, []):
                if nei == target:
                    return True
                stack.append(nei)

        return False

    def direct_referrals(self, user: str) -> Iterable[str]:
        return list(self.children.get(user, []))

    def all_referrals(self, user: str) -> Iterable[str]:
        res = []
        stack = list(self.children.get(user, []))  # direct children
        seen = set()

        # indirect children
        while stack:
            node = stack.pop()
            if node in seen:
                continue

            seen.add(node)
            res.append(node)
            for nei in self.children[node]:
                if nei not in seen:
                    stack.append(nei)

        return res


def top_k_by_reach(network: ReferralNetwork, k: int) -> list[str]:
    arr = []
    for user in network.nodes:
        reach = len(network.all_referrals(user))
        arr.append((-reach, user))
    arr.sort()
    return [user for _, user in arr[:k]]


def top_k_by_flow_centrality(network: ReferralNetwork, k: int) -> list[str]:
    arr = []

    arr.sort()
    return [user for _, user in arr[:k]]


def expected_network_size(p: float, days: int) -> float:
    if days == 0:
        return 100


