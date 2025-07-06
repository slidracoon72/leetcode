# LC - Hard

class FreqStack:
    # Stack Of Stacks (Hash Map)
    # Space: O(n)
    def __init__(self):
        # Dictionary to count frequency of each value
        self.cnt = {}

        # Variable to keep track of the current maximum frequency
        self.maxCnt = 0

        # Dictionary to map frequency to a stack of elements with that frequency
        self.stacks = {}

    # Time: O(1)
    def push(self, val: int) -> None:
        # Increase the frequency count for the value
        valCnt = 1 + self.cnt.get(val, 0)
        self.cnt[val] = valCnt

        # Update max frequency if this value exceeds current max
        if valCnt > self.maxCnt:
            self.maxCnt = valCnt
            self.stacks[valCnt] = []  # Initialize a new stack for this frequency

        # Push the value onto the stack corresponding to its frequency
        self.stacks[valCnt].append(val)

    # Time: O(1)
    def pop(self) -> int:
        # Pop the most recent element from the stack with the current maximum frequency
        res = self.stacks[self.maxCnt].pop()

        # Decrease the frequency count for this value
        self.cnt[res] -= 1

        # If there are no more elements at this frequency, reduce maxCnt
        if not self.stacks[self.maxCnt]:
            self.maxCnt -= 1

        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
