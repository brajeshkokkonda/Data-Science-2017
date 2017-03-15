#Examples taken form python.org tutorial
door_open=True
if door_open:
    print("pls come in !")
#----Numbers and Arithmetic-----
5+2
5*2
5-2
5/2
5%2
5**2
5+3*2
a=10
a
b=10+_ #works in interactive mode (takes previous value)
b
#----STRINGS-----
s='hello\nworld'
s
print(s)
print(r'C:\some\name')
3 * 'un' + 'ium'
'Py' 'thon'
a='hello '
b='python'
a+b
text=('first line '
      'second line')
text
word='Python'
word[0]
word[-1]
word[0:2]
word[:2]+word[2:]
word[2:]
'''
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
'''
word[4:42]
word[42:]
#word[0]='J' 'str' object does not support item assignment
'J' + word[1:]
s = 'supercalifragilisticexpialidocious'
len(s) #len is a built-in functon
#---------LISTS---------
squares=[1,4,9,16,25]
squares
squares[0]
squares[-1]
squares[-3:]
squares[:]
squares + [36,49,64]
#NOTE: 'str' obj is immutable, lists are mutable
x=[12,13,15]
x[2]=14
x
x.append(15)
x
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
letters[2:5] = ['C', 'D', 'E'] #replace some values
letters
letters[2:5] = []
letters
len(letters)
#nesting the lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
#First steps towards programming
#Fibinacci Series
a,b=0,1
while b<10:
    print(b,end=' ')
    a,b=b,a+b
#Swapping two numbers
a,b=10,20
a,b=b,a
a
b
#more control flow statements
x = int(input("Please enter an integer: "))
if x%2==0:
    print('Even number')
else:
    print('Odd number')
#use elif: to else if
fruits=['apple','banana','cherry']
for f in fruits:
    print(f)
for i in range(5):
    print(i)
for i in range(1,6):
    print(i)
#usage of break, continue, pass

#-----FUNCTIONS-----------
def fib(n):
    a,b=0,1
    while a<n:
        print(a, end=' ')
        a,b=b,a+b
    print()
fib(1000)
fib
f=fib
f(2000)
fib(0)
print(fib(0))
#--------------
def fib2(n):
    result=[]
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result
f100=fib2(100)
f100
#NOTE: Indentation and spacing are very important in python
#-----------------------
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
#----------------
def my_function():
    """Do nothing, but document it.

       No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)
#-------------
#using lambda expressions, function annotations
#----DATA STRUCTURES-----------
#More on Lists
my_list=[10,20,30]
my_list.append(40)
my_list.insert(2,25)
my_list.remove(25)
my_list.pop()
my_list.pop(1)
my_list.index(10)
my_list.count()
my_list.insert(1,10)
my_list.count(10)
my_list.sort()
my_list.reverse()
#List as STACK
stack=[3,4,5]
stack.append(6)
stack.append(7)
stack
stack.pop()
stack
stack.pop()
stack
#List as QUEUE
from collections import deque
queue=deque(["Eric","John","Michel"])
queue.append("Terry")
queue.append("Graham")
queue
queue.popleft()
queue.pop()
#List Comprehensions
squares=[]
for x in range(10):
    squares.append(x**2)
squares
squares2=list(map(lambda x:x**2, range(10)))
squares3=[x**2 for x in range(10)]
#Nested List Comprehensions
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]
[[row[i] for row in matrix] for i in range(4)]
#Using del stmnt
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
del a[2:4]
del a[:]
del a #see variable explorer for effect
#Using tuples ans sequences
#SETS

#DICTIONARIES
tel = {'jack': 4098, 'sape': 4139}
tel['guido']=4127
tel
del tel['sape']
tel['irv']=4127
tel
list(tel.keys())
sorted(tel.keys())
'guido' in tel
dict([('ana',111),('barbara',222),('christina',333)])
{x: x**2 for x in (2, 4, 6)}
#Looping Techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)
for i,v in enumerate(['tic','tac','toe']):
    print(i,v)
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
for i in reversed(range(1,5,1)):
    print(i)
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
for i in range(5,0,-1):
    print(i)
#-----Modules------
'''
write a python script with functions, name it fibo.py
place the above file in os.getcwd()
import fibo
fibo.fib(100)
from fibo import fib, fib2
from fibo import *
>>>python fibo.py <arguments>
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
-------
dir()
dir(fibo)
packages
'''
#---------------INPUT and OUTPUT-------------
print('{0} and {1}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))
#reading and writing files
f=open('workfile','w')
f.write('This is a simple file\n')
f.close()
with open('workfile','r') as f:
    read_data=f.read()
f.closed
import json
json.dumps([1,'simple','list'])
#see pickle also
#--------------ERRORS & EXCEPTIONS------------
while True:
    try:
        x=int(input("Please enter a number: "))
        break;
    except ValueError:
        print("Oops! That was no valid number. Try again...")
raise NameError('HiThere')
#--------------CLASSES---------------------
class Complex:
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart
x=Complex(3.0, -4.5)
x.r, x.i
#inheritance
class A:
    def disp():
        print("hello from class A")
class B(A):
    def test():
        print("hello from class B")
B.disp()
B.test()
#Iteratiors
s='abcd'
it=iter(s)
next(it)
next(it)
#---
class Reverse:
    def __init__(self,data):
        self.data=data
        self.index=len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index==0:
            raise StopIteration
        self.index=self.index-1
        return self.data[self.index]
rev=Reverse('spam')
iter(rev)
for char in rev:
    print(char)
#Generators
def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]
for char in reverse('golf'):
    print(char)
#Generator expressions
sum(i*i for i in range(10))
xvec=[10,20,30]
yvec=[7,5,3]
sum(x*y for x,y in zip(xvec,yvec))
#---
import math
math.pi
math.factorial(3)
#Standard Library
import os
os.getcwd()
os.chdir('/myfolder')
os.system('mkdir spyder')
dir(os)
help(os)
import shutil
dir(shutil)
import glob
glob.glob('*.py')
#command line args
#>>>python demo.py one two three
import sys
print(sys.argv)
#string pattern matching (regular expr)
import re
re.findall(r'\bf[a-z]*','which foot or hand fell fastest')
#mathematics
import math
math.cos(math.pi/4)
math.log(1024,2)
import random
random.choice(['apple','pear','banana'])
random.sample(range(100),10)
random.random()
random.randrange(6)
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
statistics.median(data)
statistics.variance(data)
#Dates and Times
from datetime import date
now=date.today()
now
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
birthday = date(1983, 4, 28)
age = now - birthday
age.days
'''
Other Libraries include:
    zlib, timeit, doctest, unittest, json, sqlite3, reprlib, pprint, textwrap,
    locale, string, time, struct, threading, zipfile, logging, weakref, gc, 
    array, collections, bisect, heapq, decimal
'''
#----Virtual Environments and Packages
#>>>python3 -m venv tutorial-env
#using pip
'''
pip search astronomy
pip install novas
pip install requests==2.6.0
pip install --upgrade requests
pip uninstall <packages>
pip show
pip show requests
pip list (displays all pkgs)
'''
#HAPPY CODING BAJJU :)