
## MIT 6001 class notes


def main():
    x = int(input("enter a number"))
    for i in range(x):
        print(i)
    print("Done")

## main()
## bool,int,float,string

name = 'Aaron'
print(3*name)
length = len(name) ##length

print('Aaron'[3]) ##indexing

'Aaron'[1:3] ## slicing

'a' in "Aaron" ## checks for membership

num = int(input("enter a number"))
while num == 5:
    print('Wrong Choice!')
    num = int(input("enter a number"))
print('Finally a good number')

for n in range(5):
    print(n)

mysum = 0 
for i in range (1,20,3):
    mysum +=i
    ## break will exit us from loop
print(mysum)

if char in letters: ## checks if character is in another string

    |guess**3|-cube <= epsilon ## checking if answer is close enough to the value we want

    while abs(guess**3 - cube)>= epsilon and guess <= cube:


## BI-section search
    set up variables and set ans = (high+low)/2


print("Hi",end='')
print("there")

 /= divide normally
 % = remainder after dividing
 // = how many time it divides evenly

 Functions - have names, parameters, docstrings, body

 def function_1(param1):
    """
        Input param, a positive num int
        returns True if even, otherwise false    
    """
    print('Hi')

    return param1 % 2 == 0 ## return will be the output of the function 

function_1(1,2)

return will act like a break and throw us out of the function

one function can call another

def func2(firstname,lastname, reverse=True):    # giving default value to reverse if not specified in func call

    using """
    returns true if 1 is passed in
    """     # we can give a function a docstring so we can show what the inputs are and what is expected to happen


    ### string methods https://docs.python.org/3/library/stdtypes.html#string-methods

    ## recursive code for multiplication
    
    def mult(a,b):
        if b ==1:
            return
        else:
            return a + mult(a,b-1)


 if we have a file circle.py
    in circle.py 
        pi = 3.1454
        def area(radius):
            return pi*(radius**2)
        def circumfrence(radius):
            return 2*pi*radius

in different file we can import and use things in cirlce.py 

import cirlce  ## importing module circle.py
pi = 3 ## reassigning pi

print(pi)
print(cirlce.pi)
print(cirlce.area(3))
print(cirlce.cirumcfrence(3))

from cirlce import *  ## this imports all functions and variables from cirlce so we don't need to ur cirlce.pi to refer to the pi defined in the circle.py file


nameHandle = open('filename','w') ## creates a file named filename and allows us to write to it

name = input('enter your name')
filename.write(name +'\')
filename.close()


monthlyInt = annualInterestRate/12
lower = balance/12
upper = (balance*(1+(annualInterestRate)))/12

def lowpay(upper,lower):
    minpay = (upper+lower)/2
    newbal=balance
    month = 0
    while month <12:
        unpaidbal = newbal - minpay
        newbal = unpaidbal + (monthlyInt*unpaidbal)
        month+=1
    if newbal == 0:
        return minpay
    else:
        if newbal >0:
            return lowpay(upper,(upper+lower)/2)
        else:
            return lowpay((upper+lower)/2,lower)

print(lowpay(upper,lower))


## Tuple are ordered sequence of elements, w mixed types, immutable

## tuple
tuple = ()
tuple2 = (1,"three",2.0)


##tuples are great to swap variables
(x,y) = (y,x)

 return aTup[::2]

 ## list similar to tuple but are mutable and denoted with brackets []

 #list opertations
    .append(thing to append)
    .extend(add aditional list to end of list)
    .del(specific element based on index)
    .pop(returns element)
    .remove(removes specific item)

(string) ## will convert every element in string to an element in list
.split(split list at designated points making everything else one elemtn)
''.join(list) #converts list back to string w no spaces

sort() will sort the list and mutated
sorted() will sort and make a new version

everything in python is an object


I can have multiple variables pointing to the same list
warm = ['red','yellow','orange']
hot = warm ## hot points to the same data structure as warm
hot.append('pink')

xhot = warm[:] ##creates a copy of warm

copy a dic with dict.copy()


## we can use functions as inputs to a function as well as lists as inputs to functions
or we can have a list of functions and iterate over that list of functions






map(function,[list of values]) ## map allows us to return the value of the function applied to every element in the list

for elt in map(abs,[1,-2,3,-4]):
    print(elt)

    we can also feed map multiple lists and it will perform the function on each item in each list and can compare the 2





dictionaries # the index is custom indexed through a label (key) which is matched to an element, similar to and index refers to an element in a list
## dictionaries store key value pairs

my_dict = {}
grades = ['Ana':'B','Aaron':'A+','John':'C-'] ## not in any order
grades['Aaron'] ## will return 'A+'
grades['Yerong'] = 'A+'

'John' in grades ## Returns true
del(grades['Ana'])

grades.keys() ## iterable returns all keys
grades.values()




we can use dictionaries to store data we have already calculated and return it when called
global ## this term will allow a variable to be accessible outside a function



testing our code is an important part of class
    We need to test, creat defensive programming, and do debugging
defensive programming
    write specifications, modularaize, and check conditions
    think about how can i break my program?

once code runs write a set of values and expected results

unit testing: testing each individual module; regression testing
integration testing: making sure that all the units work together as expected

black box testing: explores all paths through code

overt bugs vs covert bugs
persistent vs intermittent bugs

exceptions - what happesnwhen execuction hits unexpected condition

raise - a python function to share an error message
handlers for execptions

try: ## keyword to try to execute the code
        if this code works well the code goes through if not we can use an except statement
except:
        do this when exception error

except ValueError:
        print("Could not convert")
except ZeroDivisionError:
    print('0 div')
except:
        print('Default')
else:
    ##this part will execute if there are no errors in the try statement

finally:   
    always executed after try and else and except even when they return a break or return or an error happens


while True:
    try:
        n = input("please enter integer")
        n = int(n)
        break
    except ValueError:
        print("Please enter an integer and try again")

raise ValueError('Something is wrong')

assertions - used to make sure that we raise an error if assumptions are not met


assert not len(grades) == 0, 'no grades data'
return sum(grades/ken(grades))

assertions can be used on inputs and outputs to check values


creating a class we need
to define class name, define its attributes

using a class involves create new instances of objects
doing operations on the instances

class keyword to give it name, give it coordinate, and give it class parent
    class Coordinate(object):
        define attributes
        ## similar to def, coordinate is a subclass of object, object is a superclass of coordinate


the object are data and procedures that belong to the class

methods will be like functions that only work with this class

# creating and instance of object with __init__ to initialist some data attributes
class Coordinate(object):
    def __init__(self,x,y): ##self is a parameter to refer to an instance of the class, x and y is data to initialize a coordinate object
        self.x = x
        self.y = y


c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c.x)
print(origin.x)


METHODs are like functions that only work with this class
python always passes the object as the first arguement
the . operator is used to access any attribute

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**.05


aside from self and dot notation, methods behave just like functions( take params, do operations, return values)

c = Coordinate(3,4)
origin = Coordinate(0,0)

print(c.distance(origin))


__str__ method for a class allows us to customize print statments

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**.05
    def __str__(self):
        return "<"+str(self.x) +","+str(self.y)+">"


print(c)

print(isinstance(c,Coordinate))


class fraction(object):
    def __init__(self,numer,denom):
        self.numer= numer
        self.denom = denom
    def __str__(self):
        return str(self.numer)+ '/'+ str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self,other):
        numerNew = other.getDenom()* self.getNumer()+ other.getNumer()*self.getDenom()
        denomNew = other.getDenom()* self.getDenom()
        return fraction(numerNew, denomNew)


oneHalf = fraction(1,2)

oneHalf.getNumer() ##returns 1

a class is a blue print to create an object. an instance of a class is a particular object with its associated data
instance variable contain data unique to each instance
the self arguement refers to the particular isinstance




class Employee:
    def __init__(self,first,pay,pet):
        self.fname = first ## we are setting the variable fname(which is specific to the instance because of the self. to the arguement passed in for first)
        self.pay = pay
        self.pet = pet
        self.email = first+'@company.com'
    def namepay(self): ## self refers to the specific instance which is automatically passed when called
        return '{} {}'.format(self.fname,self.pay)

emp1 = Employee('Aaron',50000,'Fimp') ## the emp1 is the instance and it gets passed automatically
## emp1.first = 'Aaron'
## emp1.pay = 50000  
print(emp1.email) ## dont need () after email since we are getting an attribute not calling a method

## methods are just functions inside of a class that perform an action on a class

print(emp1.namepay() ## emp1 is the instance
print(Employee.namepay(emp1)) ## same thing as line above, but we pass in the instance as as the arguement



class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None
    def get_age(self): ## getters return data to user without accessing the data directly
        return self.age
    def get_name(self): ##setter changes the value of a stored value
        return self.name
    def set_age(self,newage):
        self.age = newage
    def set_name(self,newname="No Name"):
        self.name = newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)

mypet = Animal(3)


Heirarchy of classes, having classes within classes

Parent class (superclass)
    child(class)
        inherits all data and behavior of parent class
        add more info



class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None
    def get_age(self): ## getters return data to user without accessing the data directly
        return self.age
    def get_name(self): ##setter changes the value of a stored value
        return self.name
    def set_age(self,newage):
        self.age = newage
    def set_name(self,newname="No Name"):
        self.name = newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)

class Cat(Animal):
    def speak(self):
        print("meow")
     def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)


class Person(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age)
        Animal.set_name(self,name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("Hello")
    def age_diff(self,other):
        diff = self.get_age()-other.get_age()
        return diff



aaron = Person('Aaron',23)


import random

class Student(Person):
    def __init__(self,name,age,major=None):
        Person.__init__(self,name,age)
        self.major = major



class variables are created before init and shared among all instances of class


class Rabbit(Animal):
    tag = 1
    def __init__(self,age,parent1=None,parent2=None):
        Animal.__init__(self,age)
        self.parent1=parent1
        self.parent2=parent2
        self.rid=Rabbit.tag
        Rabbit.tag+=1
        ##tag used to give a unique ID to every rabbit instance
        def get_rid(self):
            return str(self.rid.zfill(3))
        def __add__(self,other): ## defining + operator and what that means
            return Rabbit(0,self,other) 


r4 = r1+r2


pass will allow us to pass by adding in methods if inheriting from superclass

generators have a next() method which starts/resumes execution of the procedure. inside generator:
    yield suspends execution and return from a generator raises a stop Iteration Exception
def genTest():
    yield 1
    yield 2

foo = genTest()
foo.__next__()

for n in genTest():
    print(n)

def genFib():
    fibn_1 = 1
    fibn_2 = 0
    while True:
        next = fibn_1 +fibn_2
        yield next
        fibn_2=fibn_1
        fibn_1 = next


generators seperate concept of computing a very long sequence of objects from the actual process of computing them explicitly
allows us to generate each new object as needed

abstract notion of order of growth

import time

set up function

t0 = time.clock()
function
t1=time.clock()-t0


pylab - plotting Data 


python provides us with many libraries to guide processing and visualings fata


import pylab as plt ## allows me to reference any library procedure as plt.<procedure>


basic function plots 2 lists as x and y values

list1=[]
list2=[]

plt.plot(list1,list2)
args are lists of values, must be of the same length

overlapping displays: call multiple instances of plt.plot but not best way
plt.figure(<arg>) - creates a new display with that name if one doesnt exist already are is the name


plt.figure('1') ## creates a figure
plt.xlabel('label for xaxis')## adds xaxis lable to figure above
plt.ylabel('label for yaxis')## adds xaxis lable to figure above
plt.title('List 1')
plt.clf()## clears the figure before using it again
plt.ylim(0,1000) ##sets the bottom and top limit for yaxis
plt.plot(list1,list2, label = 'list label','b-',linewidth = 2.0)## adding label and b for blue and - to signify a line as style
plt.subplot(211) ## plots within a figure, args are number of rows, number of columns and which locatoin to use
plt.legend(loc = 'upper left')
plt.yscale('log')## changing scale of graph

plt.plot(list1,list2)
plt.figure('2')
plt.plot(list2,list1)

each figure needs its customization underneath

def displayRetireRates(month,rates,terms):
    plt.figure('retirerate')
    plt.clf()
    for rate in rates:
        xvals,yvals = retire(month,rate,terms)
        plt.plot(xvales,yvals)


