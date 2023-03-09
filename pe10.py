# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Create a list of primes
# Sum all the primes in the list

# Sieve of Eratosthenes


def writeprime(x):
    file = open('primes.txt','a')
    file.write(x+"\n")
    file.close()

x = str(3)
writeprime(x)