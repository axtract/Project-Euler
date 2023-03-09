# Sieve of Eratosthenes


testno = int(input("Enter the target number: "))

for no in range(2,testno):
    if testno % 2 == 0:
        print(f"{testno} is not prime")
    with open("primes.txt", 'a+') as file:
        for line in file:
            print(f"Testing {testno}")
            if testno % 2 == 0:
                print(f"{testno} is not prime")
                break
            elif testno % line == 0:
                print(f"{testno} is not prime")
            else: 
                print(f"{testno} is prime") 
                file.append(testno)


# Take the test number
# If the result of the division of the number by a given item in primes.txt is 0, it is not prime
# If not prime, go to the next number
# If it is prime, append it to the end of the text file
# 

