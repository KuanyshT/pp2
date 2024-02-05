def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 8, 8, 9, 11, 31]
primes = []

def filter_prime(nums):
    for x in nums:
        if is_prime(x):
            primes.append(x)
    return primes

print(filter_prime(nums))

