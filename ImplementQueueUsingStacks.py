import heapq


class MyQueue:

    def __init__(self):
        self.heap = []
        self.i = 0

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, (self.i, x))
        self.i += 1

    def pop(self) -> int:
        _, val = heapq.heappop(self.heap)
        return val

    def peek(self) -> int:
        return self.heap[0][1]

    def empty(self) -> bool:
        return len(self.heap) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
