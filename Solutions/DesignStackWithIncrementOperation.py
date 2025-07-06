class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack = [x] + self.stack

    def pop(self) -> int:
        if not self.stack:
            return -1
        else:
            ele = self.stack[0]
            self.stack = self.stack[1:]
            return ele
    def increment(self, k: int, val: int) -> None:
        if len(self.stack) < k:
            for i in range(len(self.stack)):
                self.stack[i] += val
        else:
            for i in range(len(self.stack) - k, len(self.stack)):
                self.stack[i] += val

        # Instead of if-else, can also do this:
        # for i in range(len(self.stack) - min(len(self.stack), k), len(self.stack)):
        #     self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
