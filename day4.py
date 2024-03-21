# ---> while loop
# ---> break using while loop
'''
# eg:1
# 1.)Iterate from 20 to 30 and break the loop in 27

i = 20
while i<31:
    if i ==27:
        break
    print(i)
    i+=1 # OR i+1

2.
i = 20
while i<31:
    if i ==27:
        print(i)
        break
    i+=1 # OR i+1

# ---> continue

i = 20
while i<31:
    i+=1
    if i ==27:
        continue
    print(i)

# while to iterate from 12 to 22 find the sum of all the numbers

i=12
sum=0
while i<22:
    sum=sum+i
    i+=1
print(sum)

# find the average of value from 20 to 30

i = 20
sum = 0
count = 0
while i<30:
    sum = sum+i
    count+=1
    i+=1
print(sum/count)

# ---> Nested for loop

for row in range(1, 3+1):
    for col in range(1, 4+1):
        print(row, col)

# eg:2

row=8
cols=8
for row in range(row):
    for cols in range(cols+1):
        print("*",end=" ")
    print()



sum=0
for row in range(5):
    for cols in range(5):
        sum=sum+1
        print(row,end=" ")
    print()

# to print stars in right angled triangle


for row in range(0, 6):
    for col in range(0,row+1):
        print("*", end=" ")
    print()

row=6
col=6
for row in range(0, row):
    for col in range(0, col):
        print("*",end=" ")
    print()


for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row ==0 or row ==5-1:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()


for row in range(0,5):
    for col in range(0,6):
        if((row==0 and col==3) or (row==1 and(col>=2 and col<=4)) or
                                   (row==2 and (col>=1 and col<=5))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        print()
'''
'''
for row in range(0,6):
    for col in range(0,6):
        if ((col==1 and row==1) or (col==2 and row==2) or (col==3 and row==3)
            or (col==4 and row==4) or (col==5 and row==5)):
         print("*",end=" ")
        else:
            print(" ",end=" ")
        print()

# ---> Datatypes
# primary

 number ---> int, float, complex
 string
 boolean
 none

 collection
 list
 tuple
 set
 dictionary

# --->List

1.)if the collection of elements are sorrounded by square brackets, it is consider to be list
# eg:
    l1 = [4, 7, 9, 9.89,"hello",7+9j,[8,9,10]]

# characteristics of list
1.)list have to be sorrouned by[]
2.)it is mutable ( the elements in the list are changable)
3.)Every element inside list is indexed
4.)The elements inside list will be orderd format
5.)it can hold dublicate values
6.)its heterogenous


# To acces the element in list
1 = [1,4,1,7,89,7.5,"p",,"i"]
print(l1)

#--->Indexing

In the collection datatypes list,tuple,string,the elements will be alloted 
with pre-defines unique value called index value
'''
'''
# we have two types indexing
#positive indexing ---> starts with 0 from left hand side
#Negative indexing ---> starts with -1 from right hand side

# positive indexing
1st1 = [1,4,1,7,89,7.5,"p","i"]
print(1st1[0])
print(1st1[4])
print(1st1[20])--->error


# Negative indexing
1st1 = [1,4,1,7,89,7.5,"p","i"]
print(1st1[-1])
print(1st1[-5])

# ---> slicing
1st1 = [1,4,1,7,89,7.5,"p","i"]
# lst1[start_index:end_index:step]


print(lst1[0:4])
print(1st1[6:8])
print(1st1[3:6])
print(1st1[:5])
print(1st1[3:])
print(1st1[:])


print(1st1[0:7:1]) # lst1[0:7]--->both are same
print(1st1[0:7:2])


# trail = int(input())
1st1 = [1,4,1,7,89,7.5,"p","i"]
print(lst1[-4:-1])
print(lst1[-1:-4])--> []
'''


#! To insert ot add element inside list
# append()-> used to add elelement at last position of list
11 = [9, 8, 0, 6]
11.append("car")
print(11)







            
        

















            
        

















            
        

















            
        














