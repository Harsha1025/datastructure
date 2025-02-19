# Linked lists

# A linked list is a sequence where each node points towards
# next one in the sequence and contains data points at each nodes.



        # Types of Linked list

#.1)Singly Linked Lists     last node contains null 
#.2) Doubly Linked Lists        it has 3 parameter or 3 block in node 
#.3)Circular Linked Lists          last node of list point towards to first 


# CRUD Operations on linked lists



# creating linked lists

class Node:
    def __init__(self,data,next=None):
        self.data =data
        self.next = next

class LinkedList:
        def __init__(self,head=None):
                self.head = head
       
       
       
       
        # adding elements 

class Node:
        def __init__(self,data,next=None):
                self.data = data
                self.next = next


class LinkedList:
        def __init__(self,head=None):
                self.head = head

        def add(self,data):
                new =Node(data)
                if(self.head):
                        temp =self.head
                        while(temp.next != None):
                                temp = temp.next
                        temp.next =new
                else:
                        self.head = new  # here we assing new for self.head so temp contains temp.next

               
              
# printing the list \


class Node:
        def __init__(self,data,next=None):
                self.data=data
                self.next=next

class LinkedList:
        def __init__(self,head=None):
                self.head = head

        def add(self,data):
                new =Node(data)
                if self.head:
                        temp =self.head
                        while temp.next != None :
                                temp = temp.next
                        temp.next = new
                else:
                        self.head = new
        
        def List(self,first=None):
                self.first=first
                first =self.head
                i =0
                while first:
                        i+=1
                        print(first.data)
                        first = first.next
                else:
                        print(i," end of list")




obj = LinkedList()
obj.add(1)
obj.add(2)
obj.add(3)
obj.add(4)
obj.add(5)
print("list")

obj.List()
               
               
             
        


