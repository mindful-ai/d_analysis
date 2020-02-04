# Program to calculate the average of user
# given numbers

# input
L = []

'''
n = 1

while n > 0:
    n = int(input('Enter number: '))
    L.append(n)

L.pop()
'''


n = ''
while (n != 'q'):
    n = input('Enter number: ')
    n = n.strip()
    if(n.isdigit()):
        print('Adding your number', n)
        L.append(int(n))
    else:
        print('Not adding your number', n)



print(L)
print('AVERAGE : ', sum(L)/len(L))
