def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Example usage:
# Change the value of 'number' to get different terms of the Fibonacci sequence
number = 10
fib_seq = [fibonacci(i) for i in range(1, number + 1)]
print("Fibonacci sequence up to ", number, "term:", fib_seq)
