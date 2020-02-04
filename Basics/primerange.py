import checkprime


start = int(input('Enter the start of the range: '))
end = int(input('Enter the end of the range: '))

primes = []

for num in range(start, end + 1):
    if(checkprime.checkprime(num) == True):
        primes.append(num)

print('PRIMES in the range: ')
print(primes)
