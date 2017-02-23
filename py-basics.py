# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:43:08 2017

@author: brajesh kokkonda
"""
print 'welcome to python'
#basic data types [int,float,casting,bool,complex,none]
x=10
type(x)
isinstance(x,int) 
x=3.14
type(x)
c1 = int(x)
x="hello"
type(x)
x=True
type(x)
x=2+3j
type(x)
x=None
type(x)
#containers/datastructures [list,tuple,set,dict,array,dataframe]
x=[1,2,3,4,5] #list
type(x)
x=(1,2,3,4,5) #tuple
type(x)
x={1,2,3,4,5} #set
type(x)
x={"key1":111,"key2":222,"key3":333} #dict/map
type(x)
import numpy as np
x=np.array([1,2,3,4,5]) #array
type(x)
import pandas as pd
list1=[1,2,3]
list2=[4,5,6]
x=pd.DataFrame({"list a":list1,"list b":list2}) #Data Frame
x
type(x)

#list is an indexed container that holds heterogeneous elements
list1 = [10, 30, 20, 40]
type(list1)
print list1

#create a list with elements in the range of 1 to 10 with step size of 1
list2 = range(1,10,1)
type(list2)

#sliced access to elements of list
list1[0]
list1[-1]
list1[0:2]
list1[0:]
list1[:3]
list1[0::2]
list1[0] = 100

#modifying the contents of list
list3 = []
print list3
list3.append(10)
list3.append(20)
list.insert(3,70)
list3.append(True)
list3.append(list1)

#sort the elements of list1
list1.sort()
print list1

len(list1)

#iterate through the list elements
for x in list1:
    print x
    
#tuple: immutable list
tuple1 = (10, 20, 30, 40, 50)
type(tuple1)
tuple1[0]
tuple1[-1]
tuple1[0:3]
tuple1[2] = 100

for x in tuple1:
    print x ** 2
    
#dictionary/map/associative array: a group of key-value pairs 
passengers = {100:"abc",200:"def",300:"xyz"}
type(passengers)

map1 = { "key1":10, "key2":20, "key3":30 }
        
print map1

#two ways of accessing data from map
map1.get("key4")
map1["key4"]

#adding new key-value pair
map1["key4"] = 70

#replacing value for existing key
map1["key2"] = 90

# If key doesnot exist in map, get does not throw exception whereas indexed access throws exception
map1.get("key7")
map1["key7"]

#iterate through keys of dictionary
for x in map1.keys():
    print x, map1.get(x)
    
type(map1.iteritems())

#iterate through the key-value items of dictionary
for x in map1.iteritems():
    print x

#data frames
import pandas as pd
col1 = [10,20,30,40]
col2 = ['abc','def','xyz','pqr']
col3 = [0,0,0,0]

#creating data frame
df1 = pd.DataFrame({'pid':col1,'pname':col2,'survived':col3})
df1.shape
df1.info()
df1.describe()
df1.head(2)
df1.tail()

df1['col4'] = 0

#access frame content by column/columns
df1.pid
df1['pid']
df1[['pid','pname']]
df1[[0,1]]

#dropping a column
df2 = df1.drop('survived',1)

#slicing rows of frame
df1[0:2]
df1[0:4]
df1[0:]
df1[:2]
df1[-2:]

#filtering rows of dataframe by condition
type(df1.pid > 20)
df1[df1.pid>20]

#selecting subsets of rows and columns
df1.iloc[0:2,]
df1.iloc[[0,2],]
df1.iloc[0:2,0]
df1.iloc[0:2,[0,2]]
df1.loc[0:2,['pname']]

#grouping data in data frames
df1.groupby('pid').size()

#conditional statements
for i in range(10):
    if((i+1)%2==0):print i+1

#Numbers
val1=100
del val1 #see variable explorer
pow(2,3)

#Strings
str1="Hello"
str1.lower()
str1.upper()

#DateTime and calendar
import time;
localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime
import calendar
cal = calendar.month(2017, 2)
print "Here is the calendar:"
print cal

#Functions
def hello(str):
    print "Hello",str,"!!!"
    return
hello("Thimma")

def hi(str):
    x="hi",str,"!"
    return x
print hi("bajju")

#Files and Exception handling
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"
   fh.close()

#Class
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

#Threads
import thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass