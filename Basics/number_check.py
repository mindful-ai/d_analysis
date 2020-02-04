# Program to check if a number is
# positive, negative or zero

# input

n = int(input("Enter a number: "))

# process
# output

if (n > 0):
    print('The number is positive')
    if (n % 8 == 0 ):
        print('The number is also divisible by 8')
elif (n < 0):
    print('The number is negative')
else:
    print('The number is zero')
