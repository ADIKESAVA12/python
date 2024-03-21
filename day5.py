# ---> common functions for list
'''
l1 = [6,7,8,9,0]
print(len(l1))
print(max(l1))
print(min(l1))

l1 = [6,7,8,9,"p","u"]
print(max(l1)) ---->error coz its a combination of int and string
print(min(l1)) ---->error coz its a combination of int and string


l1 = [6,7,8,9,0,8.89,-5,0.78]
print(max(l1))
# index() ---> to get index value of specific element
print(l1.index(9))

l1=[6,7,8,9,0,8.89,-5,0.78]
# count()--->how many num of times an element is repeated
print(l1.count(6))

# some functions which is specially used for list

# To add element inside list
insert(indec_value,element)--> to add element at specific index position
l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]
li.insert(2,"cars")
print(l1)

#  To delete element from list
l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]



# pop(inde_valve) --> used to delete element at specific index
'''
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
l1.pop(5)
print(l1)
'''

# remove(element) --> used to delete element directly
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
l1.remove(6.76)
print(l1)
'''
# clear() --> to complete delete all element in list
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
l1.clear()
print(l1)

del --> to delrte the list
del l1 #or del(l1)
print(l1)

# ? join 2  lists

l1 = [9, 0, 8]
l2 = ["p", "0", "t", 34]
print(l1+l2)


# or

# * extend() --> to combine 2 lists
l1.extend(12)
print(l1)

# ? ---> copy()
l1 = [6, 7, 8,9, 3]
l2 = l1.copy()
print(l2)
print(l1)

print(id(l1))
print(id(l2))
'''
'''
# difference between shallow copy and deep copy
#  shallow copy
import copy
l1 = [8,9,0,[5,6],[3,2,1]]
l2=copy.copy(l1)
l1.append(209)
print(l1)
print(l2)

# deep copy
import copy
l1=[8,9,0,[5,6],[3,2,1]]
print(l1[-1][1]) ---> to index nested list

l2=copy.deepcopy(l1)
l1[-1].append('cars')
print(l1)
print(l2)
'''
'''
# sort ---> arrange the elements in ascending or desending order
l1 = [9,7,45,0,-6,5,12]
l1.sort() # to arrange in asecending order
print(11)

l1.sort(reverse=True)
print(l1)

l1 = ['z'z,'i','o','p',9]
l1.sort()
print(l1) # -->error

# list constructor
# list() --> to conver other collection datatype to list
l3 = ((8,9,0)
print(list(l3))

l4 = (8,9)
print(list(l4))

# ---> nested list

l1 = [8,9,[0,8,7],["p","o",'y'],[8,'t']]
print(l1([-2][1])#-->0

print(l1[1:4])
print(l1[1:-1])

# to delete "t" from l1
l1[-1].remove('t')
print(l1)

# combine these ["p","o",'y'],[8,'t']] lists in  l1 to ["p","o",'y',8,'t']
l1=[-2].extend(l1[-1])
l1.pop(-1)
print(l1)
'''
'''
# ---> Tuple

1.)tuple have to be surrounded by ()
2.)The elements inside tuple are not changable
3.)The elements inside tuple are indexed
4.)The elements will execute in order
5.)It is heterogenous
6.)It allow duplicate elements

# eg:
t1 = (8,8,9,6,5.78,[9,0],(6,8),"hey", 9+6j)
print(t1)
print(type(t1))

# indexing, slicing are all same as list

# ways to create tuple
l1=[8]
print(type(l1))#list

l1=(8,)
print(type(l1))#tuple

l1=8,9
print(type(l1))#tuple

#len(),min(),max(),index(),count()--->all same as list

# to add elements inside tuple --> cannot add
# cannot delete any element from tuple

# join 2 tuples
t1 = (8,9,0)
t2 = (6,7,8)
print(t1+t2)
'''
'''
# To add all elements inside list and tuple
sum()
l1 = (8,9,7,6)
print(sum(l1))

# * sort tuple
#t1 = (8, 9,0, 89, 12)
#print(tuple(sorted(t1)))
#print(tuple(sorted(t1, reverse=True)))

# * Iterate list and tuples

# Iterate based on elements

l1 = [9, 8, 0, 6, 5]
for i in l1:
    print(i)

# Iterate based on index value

l1=[9,8,0,6,5,7,36,54,55,6,43,5,66]
for i in range(0,len(l1)):
    print(l1[i])

# --->Strings
s1 = 'o'
print(type(s1))

s1 = 'u'
print(type(s1))
s1 = "helo world"
# To access string
print(s1)
# indexing and slicing --->same as list and tuple
print(s1[0:5])
'''
'''
# --> common functions

# len(),min(),max(),index(),count()
s1="hello world"
print(len(s1))
print(max(s1))
print(min(s1))

# ord() --> used to find the ASCII value of a character

s1="u"
print(ord[s1])

# strip()---->to eliminate the space in beginning and end of string
s1=" where are you"
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())
'''
'''

# ---> strip()
# --> to eliminating the space in beginnning and end of string
# M:-1
# --> to eliminate left space
'''
s1 = "   where are you.?"
print(s1.lstrip())
'''
# M:-2
# --> to eliminate right space
'''
s1 = "where are you.?  "
print(s1.rstrip())
'''
# M:-3
# --> to eliminate right and left space
'''
s1 = "   where are you.?    "
print(s1.strip())
'''

# ---> split()-->
# --> to split the words in string based on a character
s1= "where are you.?"
print(s1.split(" "))

# Swapcase()---> to convert capital to small and small to capital

s1="HEY there"
print(s1.swapcase())


# Title() --> to write the string in format of title
s1='never giveUP'
print(s1.title())  # --> Never Giveup


# Capitalize() ---> 1st char of string will be converted to capital
'''
'''
s1='never giveUP'
print(s1.capitalize())

# Join the strings
s1 = "hello"
s2 = 'world'
print(s1+s2)

s1 = how are you
iam fine
hey there
'''
'''
# Swapcase()---> to convert capital to small and small to capital

s1="HEY there"
print(s1.swapcase())


# Title() --> to write the string in format of title
s1='never giveUP'
print(s1.title())  # --> Never Giveup


# Capitalize() ---> 1st char of string will be converted to capital

s1='never giveUP'
print(s1.capitalize())

# Join the strings
s1 = "hello"
s2 = 'world'
print(s1+s2)


# * join() -->
l1 = ["hey" ,"there"]
print(" ".join(l1))
print("$".join(l1))

s1 = "welcome to all"
print(s1.endswitch('1'))
print(s1.startswitch('w'))

s1 = "67"
print(type(s1))
print(s1.isdigit())


# * print the string in reverse manner
s1 = "Welcome to all"
print(s1[('L'))

# Eg:1
wap to find the number of lower case letters
s1 = "HEY there you aRE"
for i in s1:
      if i.islower():
      count+=1
    print("The total num of lower case lettres:",count)
'''
'''
# Eg:2 r---> "$"
s1 = 'restarter'
s1 = "IMAGIN"
fst = s1[0]
bal = s1[1:]
txt = bal.replace(fst, '$')
print(fst+txt)

str1 = "bbbbbyyybbbaaaioo"
srt2 = %
'''

# eg;3

s1 ="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy textever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containingLorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
characters = len(s1)
print(characters)

words = s1.split(" ")
print(len(words))

words = s1.split(".")
print(len(words))


sentences = s1.split('.')
for val in sentences:
    if val =='':
        index = semntences.inex('')
        sentences.pop(index)
print(len(sentences))


space = 0
for val in s1:
    if val ==" ":
        space=space+1
print(space)











