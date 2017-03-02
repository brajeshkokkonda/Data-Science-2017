def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[int(len(arr) / 2)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
    
print (quicksort([3,6,8,10,1,2,1]))

'  world '.strip()

animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)

animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print ('#%d: %s' % (idx + 1, animal))
    
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print ('A %s has %d legs' % (animal, legs))

#functions
def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print(sign(x))
    
#function demo 2
def hello(name, loud=False):
    if loud:
        print ('HELLO, %s!' % name.upper())
    else:
        print ('Hello, %s' % name)

hello('Bob') 
hello('Fred', loud=True)

#class demo
class Greeter(object):
    
    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable
        
    # Instance method
    def greet(self, loud=False):
        if loud:
            print ('HELLO, %s!' % self.name.upper())
        else:
            print ('Hello, %s' % self.name)
        
g = Greeter('Fred')  # Construct an instance of the Greeter class
g.greet()            # Call an instance method; prints "Hello, Fred"
g.greet(loud=True)   # Call an instance method; prints "HELLO, FRED!"

#numpy demo
import numpy as np
a = np.array([1, 2, 3]) 
a = np.zeros((2,2))
b = np.ones((1,2))
c = np.full((2,2), 7)
d = np.eye(2)
e = np.random.random((2,2))
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = a[:2, 1:3]

#integer array indexing
a = np.array([[1,2], [3, 4], [5, 6]])
a[[0, 1, 2], [0, 1, 0]]
np.array([a[0, 1], a[0, 1]])

a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
b = np.array([0, 2, 0, 1])
a[np.arange(4), b] # 4 rows and b col indexes

#array math

x = np.array([1, 2])
x.dtype
x = np.array([1.0, 2.0])
x.dtype
x = np.array([1, 2], dtype=np.int64)
x.dtype

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

x+y
np.add(x, y)
np.subtract(x, y)
np.multiply(x, y)
np.divide(x, y)
np.sqrt(x)

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])
v.dot(w)
np.dot(v, w)
x.dot(v)
np.dot(x, v)
x.dot(y)
np.dot(x, y)

x = np.array([[1,2],[3,4]])
np.sum(x)
np.sum(x, axis=0)  # Compute sum of each column; prints "[4 6]"
np.sum(x, axis=1)  # Compute sum of each row; prints "[3 7]"
x.T

#broadcasting
# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)   # Create an empty matrix with the same shape as x

# Add the vector v to each row of the matrix x with an explicit loop
for i in range(4):
    y[i, :] = x[i, :] + v

# Now y is the following
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]
print (y)
#Alternative way (without using loops)
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1))
vv
y = x + vv
y
#Another yet simple approach
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v

#Appplications of broadcasting
# Compute outer product of vectors
v = np.array([1,2,3])  # v has shape (3,)
w = np.array([4,5])    # w has shape (2,)
# To compute an outer product, we first reshape v to be a column
# vector of shape (3, 1); we can then broadcast it against w to yield
# an output of shape (3, 2), which is the outer product of v and w:
# [[ 4  5]
#  [ 8 10]
#  [12 15]]
print (np.reshape(v, (3, 1)) * w)
# Add a vector to each row of a matrix
x = np.array([[1,2,3], [4,5,6]])
# x has shape (2, 3) and v has shape (3,) so they broadcast to (2, 3),
# giving the following matrix:
# [[2 4 6]
#  [5 7 9]]
print( x + v)
print ((x.T + w).T)
#above line can be written as:
x + np.reshape(w, (2, 1))

#matplot lib intro (similar to MATLAB)
import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

# Plot the points using matplotlib
plt.plot(x, y)
plt.show()  
#-------------------
import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the points using matplotlib
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()

#sub-plot example
import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Set up a subplot grid that has height 2 and width 1,
# and set the first such subplot as active.
plt.subplot(2, 1, 1)

# Make the first plot
plt.plot(x, y_sin)
plt.title('Sine')

# Set the second subplot as active, and make the second plot.
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

# Show the figure.
plt.show()