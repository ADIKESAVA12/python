'''
set1 = {'Python', 'Java', 'Data Science'}
set2 = {'ML', 'AI', 'R Language', 'Python'}
set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
c = 0
flag = 0
for val in range(3):
    c=c+1
    if c==1:
        for val in set1:
            if val in set2 or val in set3:
                flag=1
                break
    if c==2:
        for val in set2:
            if val in set1 or val in set3:
                flag=1
                break

    if c==3:
        for val in set3:
            if val in
'''
'''
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = []
i = 0
while i < len(list1):
    combined_string = list1[i] + list2[i]
    result.append(combined_string)
    i += 1
print(result)

# functions
# defination:
 Function is a block of code which is used to perform a specific functionality
 Function can be created by using def keyword

# function has 3 parts
function declaration
function defination
function call
'''
'''
def greet():
    print("welcome user!!")
   
greet()
greet()
greet()
greet()
greet()
greet()
greet() # function calling
'''
# Eg:2
# Function with parameter
def greeting(name):
    print("welcome",name)

for val in  range(3):
    username = input("Enter the name:")
    greeting(username)

# Eg:3
 def profile(name,age

# 1.)Write a python script to generate and print a dictionary that contains
  a number (between 1 and n) in the form(x,x*x).
  simple dictionary(n = 5):
  expected output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi numb






















