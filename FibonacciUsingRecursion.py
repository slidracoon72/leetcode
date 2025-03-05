class Solution:
    def fibonacci(self, n):
        if n <= 0:
            return "Invalid input"
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def fibonacci_of_nth_number(self, n: int):
        if n <= 0:
            return "Invalid input"
        elif n == 1:
            return 0
        elif n == 2:
            return 1

        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b

        return b


# Change the value of 'number' to get different terms of the Fibonacci sequence
c = Solution()
number = 10
fib_seq = [c.fibonacci(i) for i in range(1, number + 1)]
print("Fibonacci sequence up to ", number, "term:", fib_seq)
print(c.fibonacci_of_nth_number(10))
