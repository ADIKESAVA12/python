'''
# Eg:3
def profile(name,age,place):
    txt = "My name is {}. Iam{} years old.Iam from{}."
    print(name,age,place)
profile("sid",29,"cbe")

#Eg:4
# Function with return ststement

# return
1.)A Varaiable declared inside the function can be accessed the function
   using return
2.)return does not print anything
3.)we cannot write any code below return statement



def f1():
    z = 8
f1()
print(z) # error --> cannot use outside the function

'''
'''
def f1(a,b):
    c = a*b
    return c
# print(f1(6,8))
obj = f1(6,8)
obj1 = f1(4,6)

def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

# problem:1

def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n, "palindrome")
    else:
        print("Not palindrome")
a = int(input("Enter the value: "))
palindrome(a)

positional args
keyword args
default args
varaiable length args
keyword varaiable length args
'''
'''

# Positional args

# Eg:1
def profile(name,phone,mark):
    txt = "My name is {}. My phone number is {}.  got {} marks."
    print(txt.format(name,phone,mark))

# eg:2
To overcome the disadvantages of position args, we use keyword args
it is the process of initialising the parameter with args while calling the
# funtions
def profile(name,phone,mark):
    txt="My name is{}. My phone number{}. I got{} marks."
    print(txt.format(name,phone,mark))
profile(name="adi",mark=100,phone=7355783657)

# ---> Exception of keyword args function
def profile(name,phone,mark):
    txt = "My name is {}.My phone number is {}. I got {} marks."
     print(txt.format(name,phone,mark))

# profile(name = "adi", mark=99, phone=9876543210) # Error
# profile(9876543210,name= "adi", mark=99) # error
profile("adi",mark=98,phone=9876543210)

# Default args
def profile(name,phone,place="kadapa"):
    txt = "My name is {}.My phone number is {}. I am from {}."
    print(txt.format(name,phone,place))

profile("sid",7464854773,"guntur")


Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal

Exception
profile(name,place="KADAPA",phone):# error--> coz default args should not follow
                                   # positional param
if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
     txt="My name is{}. My phone number{}. I got{} marks{}."
     print(txt.format(name,phone,place))
    else:
        print("You are not eligible to Signup")
file("Adi",9876543210)

# varaiable length params
# Eg:1
To pass more than 1 arg to a parametr mens we use variable length args
To convert normal paremeter to variable length param,add * to the prefix of param

name = "Adi", " Charan ", " NAresh "
#print(name)


def profile(*name):
    for val in name:
        print(" My name is",val)
profile("Adi", 'name2', 'name3')


# Eg:2

def profile(name,age):
    for val in name:
        print("My name is", val,"My age is",age)
print("My name is", val,"My age is",age)("kalyan",'name2','name3',28) # error ---> age has no args
'''
'''

def profile(name,age):
    for val in name:
        print("My name is", val,"My age is",age)
profile(28,"Adi")
'''
'''
# Keyword varaiable length args
kwargs ---> which is used to provide the args in the form of key value pair.
# Eg:1
def price(**price list):
    print(price_list)

price(shirt=1000, iphone=80000)

n = 5
{1:1,2:4,3:9,4:16,5:25}

n = int(input("Enter the number: "))
d1 = {}
for val in range(1,n+1):
    d1[val] = val**2
print(d1)


d1 = {"a":100,"b":200, "c":300}
d1 = dict(a=100,b=200,c=300)
print(d1)


# object oriented programming
The paradigms of objects oriented programming are

class
objects
inheritance
polymarphism
abstraction
encapsulation

# Class is a blue print of an object
l1 = [1,2,3,4,5,6,]

# Eg:1
class c1:
    name1 = "Adi"
    print(name1)
    

# Eg:2
class person:
    name = "Adi"

c = person() # c as object
The process of creation an object is called as Instantiation
print(c.name)

# Eg:3
# create of a method
# when the function is created with a class is called as method

class person:
    def display():
        print("Hello welcome to classes")

p = person()
p.display()

# Eg:4
# Method with parameter
class person:
    def dispaly(person,name,age):
        print(name, age)

p = person()
p.display("adi",28)
'''
# Eg:5
class person:
    fname = "adi"  
    lname = "T"

    def display(self):
        print(self.fname+""+self.lname)


p=person1()
p.first_name()
p.full_name()

# Eg:6
# constructors ---> __init__()
This is a special method which has the ability to execute itself without
calling it manually through the process of instantiation

class profile:
    def __init__(self): # constructor method
        print("hey")
        
p = profile() # through thid process











