# Eg:3
# Take values of length and breadth of a user and check it is square or not
"""

length = int(input("enter the lentgh value"))
breadth = int(input("enter the breadth value"))
if length==breadth:
    print("its a square")
else:
    print("its not a square")

# Eg:4
# python program to check whether the given integer is a multiple of both % and 7


n = int(input("enter the number:"))
if n%5==0 and n%7==0:
    print("yes")
else:
    print("no")

# Eg:5
# write a program to accept the cost price of a bike and display the road tax to be paid
# according to the fopllwing criteria :

                                   
price = int(input("enter the price:"))
amount = 0
if price>=100000:
    dicount = price*(6/100)
    value = price-discount
    tax = value*(15/100)
    total=value+tax
else:
    tax = price*(5/100)
    total = price+tax
print("The on road cost of the bike is; ",total)

# if else program
# Eg:1
a = 7
b = 9
c = 30

if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
elif c>a  and c>b:
    print("c is greater")

# A school has following rules for grading systems
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.


mark = int(input("enter the marks:"))
if mark>=80 and mark<=100:
    print("A")
elif mark>=60 and mark<80:
    print("B")
elif mark>=50 and mark<60:
    print("C")
elif mark>=40 and mark<50:
    print("D")
else:
    print("fail")


# --> short hand if else
#Eg:1
a = 9
b = 60
if a>b:
    print("A")
else:
    print("B")
"""
'''
# ---> using short short hand using if else
#* Rules
1.) statement inside the if condition have to be present at first
2.) elif cannot be used in short hand if else
3.) Always it have to end with else
'''
'''
# code to check the givenm char is vowel or consonent
char = input("enter the char;")
if char =="a" or char =="e" or char =="i" or char "o" or char =="u":
    print("it is a vowel")
else:
    print("its consonent")
#  or

str1 = "aeiouAEIOU"
if char in str1:
    print("vowel")
else:
    print("consonent")

# shorthand if else
char = input("enter the char;")
str1 = "aeiouAEIOU"
print("vowels")if char in str1 else print("consonent")

'''
# ---> elif ladder using short hand if else
# Eg:1
# find among greatest variables using short hand if else
a = 8
b = 5
c = 9

print("A is greater")if a>b and a>c else print("B is greater")if b>a and b>c else print("c is greater")
'''
# ------> looping
looping can be implemented using
for loop
while loop

# ---> for loop
for loop is ised for iteration, if we know the number of times the loop have to run
It is used to iterate the iterables eg(string, list, tuple, etc...)

# ---> syntax for loop

# syntax in c
for(i=0;<10;i++){
    printf("hello")
}

# for syntax in python
for userdefined  variable in range(start, end, step):default step value is 1
#   statement
#   statement
#   statement
'''
# Eg:1
#To print the value from 1 to 10 using for loop
'''
for i in range (0, 10): #(n, n-1)
     print(i)
     print("hello")

#eg:2
for val in range(23,50,2):
    print(val)

for val in range(1,15,3):
    print(val)

#eg:3
    
# To decrement the value
'''
'''
for val in range(10, 0, -1):
     print(val)

# eg:4
# print the output of multipilication table from 21 to 43

for val in range(1, 10+1):
    # print('7','x',val,'=',val*7)#---> method-1

    # ---> method-2
    ans="7x{}={}"
    print(ans.format(val, val*7))


#Eg:5
# brake---> used to terminate the loop

for val in range(1, 10):
    if val ==6:
        break
    print(val)

# Eg:6
for val in range(13,60, 15):
    if val ==60:
       print(val)
       break

# practise problems
# print the even numbers between 20 to 40
'''
'''
for  i in  range(20, 41,2):
    print(i)

# ---> while loop
while loop is used when we do not know the number of times the loop have run 
to itrerate the non iterable elements while loop is used 

# todo syntax

 initialisation
 while condition
    statement
    incre or decre
# eg:1
to iterate number from 1 to 10

i = 0
while i<11:
    print(i)
    i=i+1 # OR i+1
    
# for loop practice
# write a program to display sum of odd numbers and even numbers that fall between 
  12 and 37(including both numbers)
'''
for i in range(12, 37):
    print(i)
    
#----> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 43






















    

    
