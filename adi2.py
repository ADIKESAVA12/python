a=b,c=7,8
print(a,b,c)



# ----> swapping of variables

#Eg-1:

a = 7
b = 5

c = a        #c=7

a = b        #a=5
b = c        #b=7


# a=5, b=7
print (a,b)



#Eg:


a=a+b  #a=12
b=a-b  #b=12-7=5
a=a-b  #a=12-5=7


print(a,b)


a,b=b,a   #only in python
print(a,b)


a=a*b   # a=35
b=a/b   # b=35/7=5.0
a=a/b   # a=35/5=7.0

print(int(a),int(b))


# id function which is used to find the memory address of the variable

a = 7
print(a)
print(id(a))


#----> Keywords

# Keywords are reserved words which provides special meaning to
# compiler or interpretor


import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))


# To check if the string is keyword or not

print(keyword.iskeyword("sid")) #False








# ----> Literals

#Literal is the constant value assigned to the variable.
#A variable is considered to be constant when it is defines capitals.

 
a=78   # a is variable
A=78   # A is constant


n1=89+7j
print(hash(n1))

#f1=[2,3,4]
#print(hash(f1))  #error --> list is non-constsnt or mutable datatype



# ---> Operators:

#Operators are symbols which is used to perform various operations between two or more operands.


#Arithmetic
#Assingment
#Logical
#Relational or Comparison
#Bitwise
#Identify
#Membership


# ---> Arithmetic :  (+,-,*,/,%,//,**)

#Eg:

a=8
b=6
c=9
print(a+b+c)



#input() --> which is used to get the runtime input
# eval() --> used to get the runtime values of all datatype


n1=input("enter the value: ")
print(type(n1))



a=4
b=2
print(a/b)  #to get the quotient value
print(a%b)  # to get the remainder value


# ! // --> floor division

a = 765433
b = 19
print(a//b) # ---> the output will be integer & the output will be based on the floor value

#! **--> used for power of a number

print(2**4) #--> 16

# ! Assignment --> +-=, -=, /=, *=, //=, **=, &=,|=


a= 8
a+=2
print(a)


a=30
a-=5
print(a)

# ! comparison --> ==, >, <, !=, <=, >=
a = 8
b = 7
print(a>b)


a = 9
b = 5
print(a==b)


# ! Bitwise operator --> &, |,^,~,<,>>

a = 7
b = 6
print(a|b)


# ! Logical
# and, or, not
a = 6
print(a>3 and a<10)
print(a>7 or a<30)
print(not(a>8 and a<10))

#! identity operator
 # is, is not
 # a = 8
 # b = 8
 # print(a is b)
 # print(a==b)

 # a = [1, 2, 3]
 # b = [1, 2, 3]
 # print(a is not b)

 # ! Membership operator
 # in, not in

 # li = [7,8,9,0,6,5]
 # num = 55
 # print(num in 11)
 # print(num not in 11)

 # num = 678
 # print(8 in num) # error


 # ! conditional statment
 # if, else else
 
 # Eg:1
 
 # ---> C syntax
 #  if  condition:
 #      statement
 #      statement
 #      statement
 #      statement


 # Eg:1
  # a = 6
 #  if a:
      print("hello")

 # Eg:2
 # a = 6
 # if a>3:
     print("hey")
 else:
     print("no")


 # Eg:3
   if 7>8:
       print("hello")


   print("no")

 # eg:4
   a = 0
   a = None
   a=False
   a=""
   if a:
       print("yes")
   else:
       print("no")


 # a number is even or odd
 n=int(input("enter the number value:"))
 if n %2==0:
       print(n,"is even")
 else:
       print(n, "is odd")

 name =input("enter the name:"))
 age = int(input("enter the age:"))
nationality = input("enter  the nation:"))
 if age >18 and nationality=="indian":
     print("eligibity for vote")
 else:
     print("not eligible")
     
     
     
 

 
       
 
      

