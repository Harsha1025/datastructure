# an array can be defined as a storage or container or similar items place in 
#contiguous memory locations.


    # Homogenneous array different in array 
    # Heterogeneous arry different in list


import array as myarray


#creating array

arr=myarray.array('i',[2,3,4])
arr1=myarray.array('d',[1.0,30.3,4.5,5.6,9.0])# same as below 'd'
arr2=myarray.array('u',['a','b','c','d']) #'u' is used behalf of the unicode or datatypes 


# typecodes means datatypes
print(arr.typecode)
print(arr1.typecode)
print(arr2.typecode)
# first look at the array

print(arr)
print(arr1)
print(arr2)


# printing the length of the array


for i in range(0,len(arr)):
    print(arr[i], end=" ")#In Python, the end=" " parameter in the print() 
                                    #function allows you to specify what should be printed at the end of each print() statement. By default, the print() function adds a newline character (\n) at the end of each output, moving the cursor to the next line.

print("\n")


for i in range(0,len(arr1)):
    print(arr1[i],end=" ")
print("\n")


for i in range(0,len(arr2)):
    print(arr2[i],end=" ")

print("\n")
# Accessing elements from an array using index values

x =list(range(1,100,2))

new_array = myarray.array('i',x)

# printing the array

for i in range(0,len(new_array)):
    print(new_array[i],end=" ")
print("\n")


# accessing the element at index "25"
print(new_array[27])

# adding elements in an Array

new_array = myarray.array('i',[2,3,4,56,4,67,8,95,7,68,6])

for i in range(0,len(new_array)):
    print(new_array[i],end=" ")
print(end="\n")

#adding elements in the array using insert method
new_array.insert(0,1)
new_array.insert(0,2)
# printing the new array
for i in range(0,len(new_array)):
    print(new_array[i], end=" ")
print("\n")

# adding elements using the append method
new_array.append(7)
new_array.append(8)

for i in range(0,len(new_array)):
    print(new_array[i],end=" ")
print("\n")



new_array =list(range(0,8,1))
new_array=myarray.array('i',new_array)
print(new_array)

new_array.insert(2,2)
new_array.append(3)
print(new_array)

new_array[3]=00
print(new_array)



#   DELETING elements from the array providing index on function parameter

print(new_array.pop())

new_array.pop()
new_array.pop()
new_array.pop()
new_array.pop()
new_array.pop()
for i in range(0,len(new_array)):
    print(new_array[i],end=" ")
print("\n")

# deleting elements  using the remove method

# print(new_array.remove(1))

new_array.remove(1)
print(new_array)
new_array.remove(0)
print(new_array)


# SLICING ON ARRAY

# slicing is the process of getting a sequence from the data structuree which
# will have a starting index and an ending index. Since, python arrays
# provide indexing ,slicing operatoions provide usage of array

x=list(range(0,100,3))
arr=myarray.array('i',x)

print(arr)

#slicing 

arr0 =arr[10:20]
for i in range(0,len(arr0)):
    print(arr0[i],end=" ")
print()
print(type(arr0))
 

 # we can use negative index in slicing 

arr0=arr[10:-3]
print(arr0)

#reversing the order using slicing 

arr0 = arr[::-1]
for i in range(0,len(arr0)):
    print(arr0[i],end=" ")
print("\n")


# Searching operation in an array using index()
x=list(range(0,10000,2))
search_array=myarray.array('i',x)

#printing the first 10 elements from the array

for i in range(0,10):
    print(search_array[i],end=" ")

print("\n")

for i in range(0,len(search_array[0:10])):
    print(search_array[i],end=" ")
print("\n")

# searching the number 1002 in the array

index = search_array.index(1002)
res =search_array[index]
print(index,res)


# sorting operations

sort_array = myarray.array('i',[4,3,2,1,6,7,8,9,5,4,1,2,3,4,])
print(sort_array)
sorted_array =sort_array.tolist()
print(sorted_array)
#ascending order
sorted_array.sort()
print(sorted_array)



sorted_array.sort(reverse=True)
print(sorted_array)

print("\n\n\n\n")

        #numpy Arrays

    # numpy arrays
    #creating numpy arrays 

import numpy as np

arr =np.array([1,2,3,4,5])
print(arr)
print("\n")



#creating an array with all zeros 

zeros = np.zeros((2,2))
print(zeros)

# np array with all ones

ones = np.ones((2,2))
print(ones)


#CREATING  an array wiht constant values
const = np.full((2,8),5)
print(const)
print(type(const))


#creating an identity matrix
iden =np.eye(2)
print(iden)
for i in range(0,len(iden)):
    print(iden[i])
#creating an array with random values
rnd =np.random.random((2,2))
print(rnd)



# 1d ,2d, and 3d arrays in numpy
#0 dimension array
ZeroD =np.array(1)
print(ZeroD)
print("\n")
#1d array
oneD =np.array([1,1])
print(oneD)


#2d array
twod=np.array([[1,23,4,5],[34,45,67,45]])
print(twod)

#multi-dimensional array
multiD=np.array([1,2,3,4,5],ndmin=5)
print(multiD)






        # Operation on numpy 

# CRUD  operation on Numpy Arrays
#reading from a numpy array
sample_array =np.array([1,2,3,4,5,6,7,8,9])

for i in range(0,len(sample_array)):
    print(sample_array[i],end=" ")
print("\n")

#updating element in a numpy array,we make use of indexing here.
sample_array[8]=100
print(sample_array)

#Deleting elements in a numpy array


sample_array = np.delete(sample_array,8)
print(sample_array)



#searching element in a numpy array

x=list(range(0,100000,5))
simple_array=np.array(x)
print(simple_array)
print(len(simple_array))
#searching the element 5500
res =np.where(simple_array == 5500)
print(res)

#checking if the returning index is true
print(simple_array[1100])



# sorting elements in a numpy array
sample_array=np.array([9,4,2,23,45,68,90,6])
print(sample_array)
#sorting the numpy array using sort()
x=np.sort(sample_array)
print(x)

#mathematical operation on numpy arrays
a =np.array([[2,3,4,5]],dtype=np.int64)
b =np.array([[2,2,9,8]],dtype=np.int64)

# adding two numpy arrays
addition = np.add(a,b)
print(addition)
#subtraction of two numpy array
sub = np.subtract(a,b)
print(sub)
#mul of two numpy array
mul =np.multiply(a,b)
print(mul)
#div of two numpy array
div =np.divide(a,b)
print(div)
#sqrt of numpy array
sqrt =np.sqrt(a)
sqrt2 =np.sqrt(b)
print(a," \n", b)


#transpose of numpy
x =np.array([[1,2,3],[1,2,4],[3,4,5]])
transpose=np.transpose(x)
print(x)
"\n"
print(transpose)