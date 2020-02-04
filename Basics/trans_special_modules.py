Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # COMPREHENSIONS
>>> div_5_8 = []
>>> for i in range(1, 1000):
	if(i % 5 == 0 and i % 8 == 0):
		div_5_8.append(i)

		
>>> div_5_8
[40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600, 640, 680, 720, 760, 800, 840, 880, 920, 960]
>>> L = [x for x in range(1, 1000) if (i % 5 == 0 ) and (i % 8 ==0)]
>>> L
[]
>>> L = [x for x in range(1, 1000) if (x % 5 == 0 ) and (x % 8 ==0)]
>>> L
[40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600, 640, 680, 720, 760, 800, 840, 880, 920, 960]
>>> # [ expr(var) <loop(var)> <condition(var)> ]
>>> L = [x**2 for x in range(10, 20)]
>>> L
[100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
>>> T = ( (x, x**2) for x in range(10, 100) if(x % 4 == 0))
>>> T
<generator object <genexpr> at 0x000001F3D1107930>
>>> list(T)
[(12, 144), (16, 256), (20, 400), (24, 576), (28, 784), (32, 1024), (36, 1296), (40, 1600), (44, 1936), (48, 2304), (52, 2704), (56, 3136), (60, 3600), (64, 4096), (68, 4624), (72, 5184), (76, 5776), (80, 6400), (84, 7056), (88, 7744), (92, 8464), (96, 9216)]
>>> L = ['red', 'red', 'green', 'yellow', 'red', 'green']
>>> D = { color:L.count(color) for color in L }
>>> D
{'red': 3, 'green': 2, 'yellow': 1}
>>> L
['red', 'red', 'green', 'yellow', 'red', 'green']
>>> F = [color.upper() for color in L if(color == 'yellow')]
>>> F
['YELLOW']
>>> F = [color.upper() if color == 'yellow' else color for color in L]
>>> F
['red', 'red', 'green', 'YELLOW', 'red', 'green']
>>> ##############################################################################
>>> T = [12, 34, 45, 76, 100]
>>> T = ['12C', '34C', '45C', '76C', '100C']
>>> t = '12C'
>>> t[:-1]
'12'
>>> def c2f(ts):
	t = int(ts[:-1])
	f = t * 1.8 + 32
	return str(f) + 'F'

>>> F = map(c2f, T)
>>> F
<map object at 0x000001F3D109B8D0>
>>> list(F)
['53.6F', '93.2F', '113.0F', '168.8F', '212.0F']
>>> T = [12, 34, 45, 76, 100]
>>> F = [t * 1.8 + 32 for t in T]
>>> F
[53.6, 93.2, 113.0, 168.8, 212.0]
>>> ############################################################################
>>> L = list(range(1, 101))
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> L = filter(lambda x: len(str(x)) == 2, L)
>>> L
<filter object at 0x000001F3D0F952B0>
>>> list(L)
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> len(10)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    len(10)
TypeError: object of type 'int' has no len()
>>> len(str(10))
2
>>> def sum2(n):
	if(int(str(n)[0]) + int(str(n)[1]) == 10):
		return True
	else:
		return False

	
>>> F = filter(sum2, L)
>>> list(F)
[]
>>> F
<filter object at 0x000001F3D0F882E8>
>>> L
<filter object at 0x000001F3D0F952B0>
>>> list
<class 'list'>
>>> L = list(L)
>>> L
[]
>>> L = list(range(1, 101))
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> list(filter(sum2, L))
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    list(filter(sum2, L))
  File "<pyshell#58>", line 2, in sum2
    if(int(str(n)[0]) + int(str(n)[1]) == 10):
IndexError: string index out of range
>>> L = list(range(10, 100))
>>> 
KeyboardInterrupt
>>> list(filter(sum2, L))
[19, 28, 37, 46, 55, 64, 73, 82, 91]
>>> ##########################################################################
>>> T1 = ('Prem', 'Harish', 'Raghavendra')
>>> T2 = ('TCS', 'ANZ-EY', 'ANZ-EY')
>>> list(zip(T1, T2))
[('Prem', 'TCS'), ('Harish', 'ANZ-EY'), ('Raghavendra', 'ANZ-EY')]
>>> dict(zip(T1, T2))
{'Prem': 'TCS', 'Harish': 'ANZ-EY', 'Raghavendra': 'ANZ-EY'}
>>> Z = zip(T1, T2)
>>> zip(*Z)
<zip object at 0x000001F3D1157688>
>>> list(zip(*Z))
[]
>>> Z
<zip object at 0x000001F3D11573C8>
>>> Z[0]
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    Z[0]
TypeError: 'zip' object is not subscriptable
>>> Z = zip(T1, T2)
>>> list(zip(*Z))
[('Prem', 'Harish', 'Raghavendra'), ('TCS', 'ANZ-EY', 'ANZ-EY')]
>>> ################################################################
>>> L = ['red', 'green', 'blue', 'red', 'yellow', 'red', 'green']
>>> from collections import Counter
>>> z = Counter(L)
>>> z
Counter({'red': 3, 'green': 2, 'blue': 1, 'yellow': 1})
>>> ################################################################
>>> from operator import itemgetter
>>> itemgetter(1)('prem')
'r'
>>> itemgetter(1)(L)
'green'
>>> itemgetter(-1)(L)
'green'
>>> T = [ (x, x**2, x**3) for i in range(10) ]
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    T = [ (x, x**2, x**3) for i in range(10) ]
  File "<pyshell#93>", line 1, in <listcomp>
    T = [ (x, x**2, x**3) for i in range(10) ]
NameError: name 'x' is not defined
>>> T = [ (x, x**2, x**3) for x in range(10) ]
>>> T
[(0, 0, 0), (1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729)]
>>> itemgetter(1)(T)
(1, 1, 1)
>>> f = itemgetter(1)
>>> f = itemgetter(-1)
>>> f('apples')
's'
>>> f(L)
'green'
>>> L
['red', 'green', 'blue', 'red', 'yellow', 'red', 'green']
>>> f(T)
(9, 81, 729)
>>> L = ['zebra', 'cat', 'ball', 'sheep']
>>> L.sort()
>>> L
['ball', 'cat', 'sheep', 'zebra']
>>> L.sort(key=f)
>>> L
['zebra', 'ball', 'sheep', 'cat']
>>> ###########################################################
>>> from itertools import permutations, combinations
>>> permutations('ABCD', 3)
<itertools.permutations object at 0x000001F3D110D9E8>
>>> list(permutations('ABCD', 3))
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')]
>>> list(combinations('ABCD', 2))
[('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
>>> ##############################################################
>>> from datetime import datetime
>>> t = datetime.now()
>>> t
datetime.datetime(2020, 1, 18, 15, 26, 43, 704325)
>>> t.year
2020
>>> t.month
1
>>> t.day
18
>>> t.hour
15
>>> t.minute
26
>>> t.second
43
>>> t1 = datetime.now()
>>> for i in range(10):
	print(i, end='')

0123456789
>>> t2 = datetime.now()
>>> t1
datetime.datetime(2020, 1, 18, 15, 27, 20, 126250)
>>> 
>>> t2
datetime.datetime(2020, 1, 18, 15, 27, 46, 88691)
>>> t2 - t1
datetime.timedelta(seconds=25, microseconds=962441)
>>> t
datetime.datetime(2020, 1, 18, 15, 26, 43, 704325)
>>> f = "%A, %d-%B-%y %H:%M:%S"
>>> t.strftime(f)
'Saturday, 18-January-20 15:26:43'
>>> t
datetime.datetime(2020, 1, 18, 15, 26, 43, 704325)
>>> ##################################################
>>> L = ['red', 'blue' ,'green']
>>> enumerate(L)
<enumerate object at 0x000001F3D11596C0>
>>> list(enumerate(L))
[(0, 'red'), (1, 'blue'), (2, 'green')]
>>> ##################################################
>>> L
['red', 'blue', 'green']
>>> L1 = L
>>> L1
['red', 'blue', 'green']
>>> L
['red', 'blue', 'green']
>>> L.append('yellow')
>>> L
['red', 'blue', 'green', 'yellow']
>>> L1
['red', 'blue', 'green', 'yellow']
>>> from copy import deepcopy
>>> L2 = deepcopy(L)
>>> L
['red', 'blue', 'green', 'yellow']
>>> L2
['red', 'blue', 'green', 'yellow']
>>> L.append('pink')
>>> L
['red', 'blue', 'green', 'yellow', 'pink']
>>> L1
['red', 'blue', 'green', 'yellow', 'pink']
>>> L2
['red', 'blue', 'green', 'yellow']
>>> ################################################
>>> 'My name is {} and age is {}'.format('Anil', 35)
'My name is Anil and age is 35'
>>> t = 'My name is {0} and age is {1}'
>>> t.format('Prem', 30)
'My name is Prem and age is 30'
>>> t.format('Harish', 34)
'My name is Harish and age is 34'
>>> t = 'My name is {name} and age is {age}'
>>> t.format(age=45, name='Sunil')
'My name is Sunil and age is 45'
>>> t = 'My name is {name:15} and age is {age:4} and date of birth is {dob:10}'
>>> t.format('Anil', 35, '12-12-1988')
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    t.format('Anil', 35, '12-12-1988')
KeyError: 'name'
>>> t.format(name='Anil', age=35, dob='12-12-1988')
'My name is Anil            and age is   35 and date of birth is 12-12-1988'
>>> t = 'My name is {name:>15} and age is {age:<4} and date of birth is {dob:^15}'
>>> t.format(name='Anil', age=35, dob='12-12-1988')
'My name is            Anil and age is 35   and date of birth is   12-12-1988   '
>>> 
