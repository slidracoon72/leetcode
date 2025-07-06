# Monotonic Stack (Decreasing)
# Time and Space Complexity: O(n)
# Neetcode: https://www.youtube.com/watch?v=slYh0ZNEqSw
class StockSpanner:

    def __init__(self):
        # Initialize the stack to store pairs of [price, span]
        # Each element in the stack is a pair where the first value is the price of the stock
        # and the second value is the span of days for which this price was the maximum.
        self.stack = []

    def next(self, price: int) -> int:
        # Initialize the span for the current price to 1 (at least the current day itself)
        span = 1

        # While the stack is not empty and the price at the top of the stack is less than or equal to the current price
        # This means the current price can span over the days represented by these lower prices
        while self.stack and self.stack[-1][0] <= price:
            # Add the span of the top element in the stack to the current span
            # This is because the current price can span over all these days
            span += self.stack[-1][1]
            # Pop the top element from the stack as it is no longer needed
            self.stack.pop()

        # Push the current price and its computed span onto the stack
        # This is done to potentially help in calculating spans for future prices
        self.stack.append([price, span])

        # Return the computed span for the current price
        return span


spanner = StockSpanner()

# Get the span of the current day's price
print(spanner.next(100))  # Output: 1
print(spanner.next(80))  # Output: 1
print(spanner.next(60))  # Output: 1
print(spanner.next(70))  # Output: 2
print(spanner.next(60))  # Output: 1
print(spanner.next(75))  # Output: 4
print(spanner.next(85))  # Output: 6
