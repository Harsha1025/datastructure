 # stack and queue 


# this are linear data sturcture 

# stack


# implement stack in python , Using Lists

my_list =["Sunday","Tuesday","wednesday","Thrusday","Friday","Saturday"]
my_stack =[]
print(my_list)


# adding elements in the stack

for i in range(0,len(my_list)):
    my_stack.append(my_list[i])
    print(my_stack)


# removing elements from the stack

for i in range(0,len(my_stack)):
    my_stack.pop()
    print(my_stack) 


# updating elements in a stack
 
my_stack = [1,2,3,4,5,6,7,8,9]
def update(data,value):
    count=False
    for i in range(0,len(my_stack)):
        if my_stack[i] == data :
            my_stack[i] = value
            count = True
    if count == False:
            print("data is not in the stack ")
    return my_stack
    


print(my_stack)
update(9,19)
print(my_stack)



# implement stack in python - using arrays

import array as myarray

my_stack = myarray.array('i',[2,31,5,6,5,6,7,8,8,8])

#reading teh array /stack
def showStack(my_stack):
    for i in my_stack:
     print(i,end=" ")
    print("\n")



# inserting elements in the stack

my_stack.append(11)
showStack(my_stack)


# deleting elements from the stack

for i in range(0,len(my_stack)):
    my_stack.pop()
    showStack(my_stack)

# creating user defined exception
class MyCustomException(Exception):
    def __init__(self, args="Exception occurred"):
        self.args=args
        super().__init__(args)

# updating elements in a stack implemented using Array
stack = myarray.array('i',[1,2,3,4,5,5])

def update(data,value):
    count =False
    ind = 0
    try:
       for i in range(0,len(stack)):
         if  stack[i]==data :
             ind = i
             stack[ind] = value  
             count = True
             #break  # if i don't write break then it will change all occurence of data into value , if i write it will change only first occurence of the data
       if count != True :
                 raise MyCustomException("da")
    except  MyCustomException:
        print(data," is not found in the stack so we can't update ",data," to ",value)
    showStack(stack)


update(5,10)
update(100,2)
    




# implementing stack in python  -Using deque from the in-built collection package
# acutally deque is double ended queue
from collections import deque

my_stack = deque()

showStack(my_list)

# inserting elements in the stack

for i in my_list:
    my_stack.append(i)
    print(my_stack)
print("\n")

# for printing 

showStack(my_stack)

# deleting  the element from the stack

for i in range(0,len(my_stack)):
    my_stack.pop()
    print(my_stack)


# updating the element in stack implemented using deque

stack = deque([1,2,3,4,5,6,])
def update(data,value):
    try:
        ind = stack.index(data)
        stack[ind] = value
        showStack(stack)
        #raise MyCustomException()
   # except MyCustomException :
      #  print( print(data," is not found in the stack so we can't update ",data," to ",value))
    
    except ValueError:
         print(data," is not found in the stack so we can't update ",data," to ",value)
    


update(1,99)
update(43,9)




# sort in stack using array,list and deque

stack_deq = deque([23,4523,2,4,36,6,4,6])
stack_list=[3,4,53,2,2,4,5,0,67]
stack_arr = myarray.array('i',[6,4,3,2,5,6,7,5,4,3,0])

# sorting the stack implementing using deque

sample=[]
def sort_deq():
    for i in range(0,len(stack_deq)):
        x = stack_deq.pop()
        sample.append(x)
    sample.sort()
    for  i in sample:
        stack_deq.append(i)

    showStack(stack_deq)
    return stack_deq

print(stack_deq)
sort_deq()


# sorting the stack using list
sample=[]
def sort_list():
    for i in range(0,len(stack_list)):
        x = stack_list.pop()
        sample.append(x)
    sample.sort()
    for i in sample:
        stack_list.append(i)
    showStack(stack_list)
    return stack_list


print(stack_list)
sort_list()


# sorting stack using arrays

sample =[]

def sort_arr():
    for i in stack_arr:
        x = stack_arr.pop()
        sample.append(x)
    sample.sort()
    for i in sample:
        stack_arr.append(i)
    showStack(stack_arr)
    return stack_arr

print(stack_arr)
sort_arr()



# Queues


# implement queues in python - using list

my_list =["sunday","Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday"]
my_queue = []
print(my_list)


# adding elements in the stack

for i in range(0,len(my_list)):
    my_queue.append(my_list[i])
    print(my_queue)

# removing elements from the stack

for i in range(0,len(my_queue)):
    my_queue.pop(0)
    print(my_queue)

def showQueue(my_queue):
    for i in my_queue:
        print(i,end=" ")
    print("\n ")

# update the value in queue

my_queue =[1,2,3,4,5,6,7,8,9]
def update(data,value):
    count = False
    try :
        for i in range(0,len(my_queue)):
            if my_queue[i] == data:
                my_queue[i] = value
                count = True
        if count == False:
            raise MyCustomException("No data present in queue")
    except MyCustomException as e :
        print(data,"  ",e)
    showQueue(my_queue)

    return my_queue


update(3,99)
update(34,11)



# implement queues in python - Using Array

my_Queue = myarray.array('i',[1,2,3,4,5,6,7,8,9])

# reading the Queue

showQueue(my_Queue)


# inserting elements in the stack

my_Queue.append(11)
showQueue(my_Queue)


# deleting element from the queue

for i in range(0,len(my_Queue)):
    my_Queue.pop(0)
    showQueue(my_Queue)

my_Queue=myarray.array('i',[1,2,3,4,5,6,6,7,5,9])

def update(data,value,my_queue):
    ind =0
    count = False
    try:
        ind=my_queue.index(data)
        my_queue[ind] = value
        showQueue(my_queue)
    except ValueError:
        print(data,": NO data found in the queue")

update(4,88,my_Queue)
update(34,2,my_Queue)




# implement queue in python - Using Deque

print(my_list)

my_queue =deque()

# inserting elements using append()

for i in my_list:
    my_queue.append(i)
    showQueue(my_queue)

# deleting element using popleft()
for i in range(0,len(my_queue)):
    my_queue.popleft()
    showQueue(my_queue)


# inserting elements using appendleft()

for i in my_list:
    my_queue.appendleft(i)
    showQueue(my_queue)

# removing using pop()

for i in range(0,len(my_queue)):
    my_queue.pop()
    showQueue(my_queue)


showQueue(my_Queue)

update(1,34,my_Queue)
update(45,3,my_Queue)


# sorting a Queue
queue_deq = deque([3,4,3,2,2,1,6,5,4,33,2])
queue_arr = myarray.array('i',[4,3,2,4,56,67,3,2,1,4])
queue_list=[4,5,6,7,8,54,4,3,2,21,1]

sample=[]
def sort(queue_deq):
    for i in range(0,len(queue_deq)):
        if type(queue_deq) == deque:
         res = queue_deq.popleft()
        else:
                res = queue_deq.pop(0)
        sample.append(res)
    sample.sort()
    showQueue(sample)
print(queue_deq)


sort(queue_deq)

sample=[]
print(queue_arr)
sort(queue_arr)
sample=[]
print(queue_list)
sort(queue_list)