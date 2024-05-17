# Analogy of List in Python?? What is the purpose of Python List?
#List is called sequence of values ,which is similar to container that is used to hold the data .So we can store all the data placing all
#the elements in [] brackets and seperated by comma.
#Real life example of List:
# In online shopping website ,if we buy some t-shirt.In search bar we type t-shirt and all types of t-shirt comes in the page .From where we choose
# different t-shirts and add the fvourite t-shirt in the cart.Here cart is a type of list .Where we can add items as well as remove items .

a=[]
print(type(a))
#Output :<class 'list'>

#In List we can store homogenous as well as heterogenous items.
a=[11,True,'aaa',11.23]
print(a)
#Output :[11, True, 'aaa', 11.23]

#To check the datatype of list we use type() function or .__class__
print (type(a))
print(a.__class__)
#Output :<class 'list'>
#Output :<class 'list'>

#A list can also have a list inside it.In oher words,a list can also have a nested list.
a=[11,True,'aaa',11.23,['soham','debojyoti','rahul','sourav']]
print(a)
#Output :[11, True, 'aaa', 11.23, ['soham', 'debojyoti', 'rahul', 'sourav']]    

#List is a sequence ,every element of a list has an index value .

print(a[0])
#Output :11
print(a[2])
#Output :aaa

#Remember a list can also be travelled in negative direction
print(a[-1])#This is the last element of the list
#Output :['soham', 'debojyoti', 'rahul', 'sourav']
print (a[-2])
#Output:11.23

#how to check wether a datatype is mutable or immutable?Criteria?
#The common mistake that we all make is that we see the value ,if it changes we consider it mutable.But this is
#not the right approach to check wether a datatype is mutable or immutable.We have see the address.
# For example :
#-------------------------------------------------------------------------------------------------------------------------------------------------
a=100
print(type(a))
print(a)
#Output :<class 'int'>
#Output :100
#Now
a=a+100
print(a)
#Output :200
#As the value of a is changed,people must know that it is mutable.But actually it is immutable.
a=100
print (a)
print (id(a))
#Output :100
#Output :140708847968136
a=a+100
print (a)
print (id(a))
#Output :200
#Output:140708847971336
#So we can see that the address of a is different as we added 100 to it.And that means it is immutable(Because the old address is not disturbed).
#--------------------------------------------------------------------------------------------------------------------------------------------------
#Now come to List
a=[1,2,3,4,5]
print(id(a))
#Output :1757535192128
a[0]=88
print(a)
#Output :[88, 2, 3, 4, 5]
print(id(a))
#Output :1212350776384
#Though we made a change inside the list ,the address remains same ,so we can conclude that list is mutable.
#-------------------------------------------------------------------------------------------------------------------------------------------------------
a=[]
#In empty list if we try to fetch a[0],it will give "index out of range" error
#print(a[0])
#Output :IndexError: list index out of range
a=[1,2,3,4,5]
#print(a[123])
#Output :IndexError: list index out of range
#If we try to fetch a value which is out of range ,it will give "index out of range" error
#print(a[-7])
#Output :IndexError: list index out of range
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#Nested List
a=[[1,2,3],['a','b','c'],['y','p','j']]
#Now we have to find the second element of the third element
print(a[2][1])
#Output :p
a[2][1]='Soham'
print(a)
#Output :[[1, 2, 3], ['a', 'b', 'c'], ['y', 'Soham', 'j']]
#for each loop to scroll in a loop
for i in a:
    print(a)
#Output :[[1, 2, 3], ['a', 'b', 'c'], ['y', 'Soham', 'j']]
#[[1, 2, 3], ['a', 'b', 'c'], ['y', 'Soham', 'j']]
#[[1, 2, 3], ['a', 'b', 'c'], ['y', 'Soham', 'j']]

#To check wether a element is present in a list or not
print('Soham' in a)
#Output :False
print('Soham' in a[2])
#Output :True
print ('Soham' not in a[2])
#Output :False
#------------------------------------------------------------------------------------------------------------------------------------------
#Operations in List
#Concatenation
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=l1+l2
print(l3)
#Output :[1, 2, 3, 4, 5, 6, 7, 8]
l1=[1,2,3]
print(l1*10)
#Output :[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]


#Slicing
#Slicing means breaking the list or creating a sub-list
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(lst)
#Output :[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(lst[:])
#Output :[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(lst[1:5])
#Output :[2, 3, 4, 5]
print(lst[:10])
#Output :[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst[5:])
#Output :[6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(lst[2:10])
#Output :[3, 4, 5, 6, 7, 8, 9, 10]
print (lst[2:10:1])
#Output :[3, 4, 5, 6, 7, 8, 9, 10]
print (lst[2:10:2])
#Output :[3, 5, 7, 9, 11, 13, 15]
print(lst[::4])
#Output :[1, 5, 9, 13]
b=1 in lst
print(b.__class__)
#Output :<class 'bool'>

#Deleting elements from the list
print (lst)
#Output :[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
del(lst[0])
print (lst)
#Output :[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
del(lst[:8])
print (lst)
#Output :[10,11, 12, 13, 14, 15]
del(lst)
#print (lst)
#Output :NameError: name 'lst' is not defined

lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print (dir([]))
#Output:['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', 
#'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', 
#'__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
#'__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
#'__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#append
lst.append("T-shirt")
print (lst)
#Output:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'T-shirt']

#extend
flip=['mobile','laptop','earphone','headphone']
lst.extend(flip)
print (lst)
#Output:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'T-shirt', 'mobile', 'laptop', 'earphone', 'headphone']

#insert
lst.insert(10,"Soham")
print (lst)
#Output:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Soham', 11, 12, 13, 14, 15, 'T-shirt', 'mobile', 'laptop', 'earphone', 'headphone']

#sort vs sorted
g=[22,1,44,321,4,9,7,8]
g.sort()#In sort orginal array is sorted 
print (g)
#Output:[1, 4, 7, 8, 9, 22, 44, 321]
k=[22,1,44,321,4,9,7,8]
h=sorted(k)#In sorted orginal array is not sorted a new sorted array is created
print (h)
#Output:[1, 4, 7, 8, 9, 22, 44, 321]


#pop vs remove
print (k)
#Output:[22,1,44,321,4,9,7,8]
print (k.pop())#If no index it will remove last element
print(k)
#Output:8
#[22, 1, 44, 321, 4, 9, 7]
print (k.pop(3))
#Output:321
print(k)
#Output:[22, 1, 44, 4, 9, 7]
k.remove(44)
print(k)
#Output:[22, 1, 4,9, 7]


#reverse
t=[22,1,44,321,4,9,7,8]
t.reverse()
print(t)
#Output:[8, 7, 9, 4, 321, 44, 1, 22]


#All 
a=[0,1,1,2]#It performs and operations on all the elements
print(all(a))
#Output :False
a=['soham',1,1,2]
print(all(a))
#Output :True
a=['True','False']
print(all(a))
#Output :True
#a=[True,True,true]
#print(all(a))
#Output :NameError: name 'true' is not defined
a=[]
print(all(a))
#Output :True

#Any
a=[0,1,2,3,4]#It performs or operations on all the elements
print(any(a))
#Output :True
a=[False,0]
print(any(a))
#Output :False
a=[]
print(any(a))
#Output :False

#Length
a=[0,1,2,3,4]
print (len(a))
#Output :5

#Index and Count and Max and Min and Sum
a=[1,2,3,4,5,11,24,5,11,567,55,65,11,23,44]
print (a.count(11))
#Output :3
print (a.index(567))
#Output :9
print (max(a))
#Output :567
print (min(a))
#Output :1
print (sum(a))
#Output :831

#Sorting in Descending order
a=[1,2,3,4,5,11,24,5,11,567,55,65,11,23,44]
a.sort(reverse=True)
print (a)
#Output :[567, 65, 55, 44, 24, 23, 11, 11, 11, 5, 5, 4, 3, 2, 1]


#Converting String to List
name='I am Soham Mukherjee'
x=list(name)
print(x)
#Output :['I', ' ', 'a', 'm', ' ', 'S', 'o', 'h', 'a', 'm', ' ', 'M', 'u', 'k', 'h', 'e', 'r', 'j', 'e']
for i in x:
    print(i)

#output
#I
# 
#a
#m
# 
#S
#o
#h
#a
#m
# 
#M
#u
#k
#h
#e
#r
#j
#e

a=[1,2,3,4]
b=a
print (b)
#Output :[1, 2, 3, 4]
#As b is the copy of a so both are pointing to same memory location
#Ans :YES
print(id(a))
#Output :2279938654912
print(id(b))
#Output :2279938654912
#This is called aliasing ,both are pointing to same object because one object is created
a=[1,2,3,4]
b=a[:]
print (b)
#Output:[1, 2, 3, 4]
print(id(a))
#Output:1923945138752
print(id(b))
#Output:1358162565120
#This is called cloning ,both are pointing to different object