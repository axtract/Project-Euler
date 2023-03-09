# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Create a list of primes
# Sum all the primes in the list

# Sieve of Eratosthenes

sum = 0

with open('primes.txt') as primes:
    for line in primes:
        sum = sum + int(line)

print(sum)