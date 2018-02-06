Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: /Users/franchesca/Documents/ics lecture 5.py ===========
Traceback (most recent call last):
  File "/Users/franchesca/Documents/ics lecture 5.py", line 12, in <module>
    print (double(1 + 1))
  File "/Users/franchesca/Documents/ics lecture 5.py", line 10, in double
    return n * 2
NameError: name 'n' is not defined
>>> 
=========== RESTART: /Users/franchesca/Documents/ics lecture 5.py ===========
4
>>> 
=========== RESTART: /Users/franchesca/Documents/ics lecture 5.py ===========
4
HO HO 
>>> 
=========== RESTART: /Users/franchesca/Documents/ics lecture 5.py ===========
4
Traceback (most recent call last):
  File "/Users/franchesca/Documents/ics lecture 5.py", line 13, in <module>
    print(double ("HO ")) #python doesn't care that we said we will work with numbers
  File "/Users/franchesca/Documents/ics lecture 5.py", line 10, in double
    return number ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> 
=========== RESTART: /Users/franchesca/Documents/ics lecture 5.py ===========
Traceback (most recent call last):
  File "/Users/franchesca/Documents/ics lecture 5.py", line 13, in <module>
    assert double(-111) == -222
AssertionError
>>> 
=========== RESTART: /Users/franchesca/Documents/ics lecture 5.py ===========
4
HO HO 
>>> help(double)
Help on function double in module __main__:

double(number:int) -> int

>>> help(double)
Help on function double in module __main__:

double(number:int) -> int

>>> help(double)
Help on function double in module __main__:

double(number:int) -> int

>>> help(double)
Help on function double in module __main__:

double(number:int) -> int

>>> help(double)
Help on function double in module __main__:

double(number:int) -> int

>>> help(double)
Help on function double in module __main__:

double(number:int) -> int

>>> help(double)
Help on function double in module __main__:

double(number:int) -> int

>>> double(number:int) -> int
SyntaxError: invalid syntax
>>> help(double)
Help on function double in module __main__:

double(number:int) -> int

>>> help(double)
Help on function double in module __main__:

double(number:int) -> int

>>> help(double)
Help on function double in module __main__:

double(number:int) -> int

>>> help(double)
Help on function double in module __main__:

double(number:int) -> int

>>> help(double)
Help on function double in module __main__:

double(number:int) -> int

>>> double(number:int) -> int
SyntaxError: invalid syntax
>>> help(double)
Help on function double in module __main__:

double(number:int) -> int

>>> help(sum_of_double)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    help(sum_of_double)
NameError: name 'sum_of_double' is not defined
>>> help(sum_of_doubles)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    help(sum_of_doubles)
NameError: name 'sum_of_doubles' is not defined
>>> help(sum_of_doubles)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    help(sum_of_doubles)
NameError: name 'sum_of_doubles' is not defined
>>> 
=========== RESTART: /Users/franchesca/Documents/ics lecture 5.py ===========
4
HO HO 
>>> help(double)
Help on function double in module __main__:

double(number:int) -> int
    Takes an integer and returns its double

>>> help(sum_of_doubles)
Help on function sum_of_doubles in module __main__:

sum_of_doubles(number1:int, number2:int) -> int
    Take two numbers, double and sum them

>>> 
=========== RESTART: /Users/franchesca/Documents/ics lecture 5.py ===========
4
HO HO 
sum of doubles for  <function sum_of_doubles at 0x100560e18>
>>> 
=========== RESTART: /Users/franchesca/Documents/ics lecture 5.py ===========
4
HO HO 
sum of doubles for  2 and 3 is 10
>>> 
=========== RESTART: /Users/franchesca/Documents/ics lecture 5.py ===========
4
HO HO 
Traceback (most recent call last):
  File "/Users/franchesca/Documents/ics lecture 5.py", line 41, in <module>
    assert sum_of_doubles(3, 10) == 13
AssertionError
>>> 
=========== RESTART: /Users/franchesca/Documents/ics lecture 5.py ===========
4
HO HO 
sum of doubles for  2 and 3 is 10
>>> 
=========== RESTART: /Users/franchesca/Documents/ics lecture 5.py ===========
4
HO HO 
Traceback (most recent call last):
  File "/Users/franchesca/Documents/ics lecture 5.py", line 41, in <module>
    assert sum_of_doubles(3, 10) == 13
AssertionError
>>> 
=========== RESTART: /Users/franchesca/Documents/ics lecture 5.py ===========
4
HO HO 
sum of doubles for  2 and 3 is 10
>>> 
