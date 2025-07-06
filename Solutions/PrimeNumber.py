def is_prime(number):
    """Check if a number is a prime number."""
    if number <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(49))
print(is_prime(13))
print(is_prime(43423))
print(is_prime(29))
