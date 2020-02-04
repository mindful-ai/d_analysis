Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> N = 100
>>> type(N)
<class 'int'>
>>> S = 'television'
>>> type(S)
<class 'str'>
>>> F = 1.435
>>> type(F)
<class 'float'>
>>> L = ['red', 'green', 'blue']
>>> L[0]
'red'
>>> L[-1]
'blue'
>>> type(L)
<class 'list'>
>>> T = ('red', 'green', 'blue')
>>> type(T)
<class 'tuple'>
>>> S = {'a', 'b', 'c'}
>>> type(S)
<class 'set'>
>>> D = {'name':'prem', 'age':30 }
>>> type(D)
<class 'dict'>
>>> ################################################
>>> 
>>> 
>>> s = input('Enter a number: ')
Enter a number: 19
>>> s
'19'
>>> type(s)
<class 'str'>
>>> s + 10
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s + 10
TypeError: can only concatenate str (not "int") to str
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/number_check.py 
Enter a number: 12
The number is positive
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/number_check.py 
Enter a number: -10
The number is negative
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/number_check.py 
Enter a number: 0
The number is zero
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/number_check.py 
Enter a number: 16
The number is positive
The number is also divisible by 8
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/number_check.py 
Enter a number: 18
The number is positive
>>> ####################################################################
>>> # LOOPING EXPERIMENTS
>>> 
>>> for i in 'python':
	print(i)

	
p
y
t
h
o
n
>>> for i in ['red', 'green', 'blue']:
	print(i.upper(), len(i))

	
RED 3
GREEN 5
BLUE 4
>>> 
>>> for i in ('r', 'g', 'b'):
	print(i)

	
r
g
b
>>> T = ( (1, 'a'), (2, 'b'), (3, 'c'))
>>> for i in T:
	print(i)

	
(1, 'a')
(2, 'b')
(3, 'c')
>>> x,y = (1, 'a')
>>> x
1
>>> y
'a'
>>> for x,y in T:
	print(x)
	print(y)

	
1
a
2
b
3
c
>>> for x,y in T:
	print(x, end=' ')
	print(y, end=' ')

	
1 a 2 b 3 c 
>>> D
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    D
NameError: name 'D' is not defined
>>> D = {'name' : 'Harish', 'age': 25, 'company':'ANZ', 'location':'Bengaluru' }
>>> D
{'name': 'Harish', 'age': 25, 'company': 'ANZ', 'location': 'Bengaluru'}
>>> for i in D:
	print(i)

	
name
age
company
location
>>> for k,v in D:
	print(k)
	print(v)

	
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    for k,v in D:
ValueError: too many values to unpack (expected 2)
>>> D.items()
dict_items([('name', 'Harish'), ('age', 25), ('company', 'ANZ'), ('location', 'Bengaluru')])
>>> for k,v in D.items():
	print(k)
	print(v)

	
name
Harish
age
25
company
ANZ
location
Bengaluru
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10, 20))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(1, 100, 5))
[1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]
>>> D.keys()
dict_keys(['name', 'age', 'company', 'location'])
>>> D.values()
dict_values(['Harish', 25, 'ANZ', 'Bengaluru'])
>>> D.items()
dict_items([('name', 'Harish'), ('age', 25), ('company', 'ANZ'), ('location', 'Bengaluru')])
>>> set(D)
{'company', 'age', 'location', 'name'}
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/multiplication_table.py 
Enter a number: 8
8 X 1 = 8
8 X 2 = 16
8 X 3 = 24
8 X 4 = 32
8 X 5 = 40
8 X 6 = 48
8 X 7 = 56
8 X 8 = 64
8 X 9 = 72
8 X 10 = 80
>>> 
== RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/prime.py ==
Enter a number: 4
The number is not prime
>>> 
== RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/prime.py ==
Enter a number: 5
The number is prime
>>> 
== RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/prime.py ==
Enter a number: 4
The number is not prime
>>> 
== RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/prime.py ==
Enter a number: 5
The number is prime
>>> 
= RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/average.py =
Traceback (most recent call last):
  File "C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/average.py", line 6, in <module>
    while n > 0:
NameError: name 'n' is not defined
>>> 
= RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/average.py =
[]
>>> 
= RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/average.py =
Enter number: 78
Enter number: 32
Enter number: 65
Enter number: 21
Enter number: 32
Enter number: 54
Enter number: 55
Enter number: 65
Enter number: 74
Enter number: 45
Enter number: 0
[78, 32, 65, 21, 32, 54, 55, 65, 74, 45, 0]
>>> 
= RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/average.py =
Enter number: 1
Enter number: 2
Enter number: 3
Enter number: 4
Enter number: 5
Enter number: 0
[1, 2, 3, 4, 5, 0]
AVERAGE :  2.5
>>> 
= RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/average.py =
Enter number: 1
Enter number: 2
Enter number: 3
Enter number: 4
Enter number: 5
Enter number: 0
[1, 2, 3, 4, 5, 0]
AVERAGE :  3.0
>>> 
= RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/average.py =
Enter number: 2
Enter number: 3
Enter number: 4
Enter number: 5
Enter number: 6
Enter number: t
Enter number: ert
Enter number: sdfg
Enter number: adfz
Enter number: fgh
Enter number: 5
Enter number: 6
Enter number: 7
Enter number: 7
Enter number: q
Enter number: Q

Enter number: 
Enter number: 
Enter number: 
Enter number: 
Enter number: 
Traceback (most recent call last):
  File "C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/average.py", line 18, in <module>
    n = input('Enter number: ')
KeyboardInterrupt
>>> 
= RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/average.py =
Enter number: 2
Adding your number 2
Enter number: 3
Adding your number 3
Enter number: 4
Adding your number 4
Enter number: 5
Adding your number 5
Enter number: asdf
Not adding your number asdf
Enter number: azxcv
Not adding your number azxcv
Enter number: zxc
Not adding your number zxc
Enter number: asdf
Not adding your number asdf
Enter number: fd
Not adding your number fd
Enter number: sb
Not adding your number sb
Enter number: zxc
Not adding your number zxc
Enter number: q
Not adding your number q
Enter number: Q
Not adding your number Q
Enter number: 345
Adding your number 345
Enter number: 5467
Adding your number 5467
Enter number: 678
Adding your number 678
Enter number: 
= RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/average.py =
Enter number: q
Not adding your number q
Enter number: Q
Not adding your number Q
Enter number: 
= RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/average.py =
Enter number: q
Not adding your number q
Traceback (most recent call last):
  File "C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/average.py", line 25, in <module>
    L.pop()
IndexError: pop from empty list
>>> 
= RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/average.py =
Enter number: 1
Adding your number 1
Enter number: 2
Adding your number 2
Enter number: 3
Adding your number 3
Enter number: 4
Adding your number 4
Enter number: 5
Adding your number 5
Enter number: q
Not adding your number q
[1, 2, 3, 4]
AVERAGE :  2.5
>>> 
= RESTART: C:/Users/Purushotham/Desktop/Clients/HRP-DS-ML/Basics/average.py =
Enter number: 1
Adding your number 1
Enter number: 2
Adding your number 2
Enter number: 3
Adding your number 3
Enter number: 4
Adding your number 4
Enter number: 5
Adding your number 5
Enter number: q
Not adding your number q
[1, 2, 3, 4, 5]
AVERAGE :  3.0
>>> 
