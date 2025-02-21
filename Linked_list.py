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
               
                                                                                # LinkedList
             
        
# inserting values in a linked list  -in the beginning

class Node:
        def __init__(self,data,next=None):
                self.data=data
                self.next=next

class LinkedList:
        def __init__(self,head=None):
                self.head = head


        def add(self,data):
                new =Node(data)
                if(self.head):
                        temp =self.head
                        while(temp.next):
                                temp = temp.next
                        temp.next = new
                else:
                        self.head = new



        def List(self,current=None):
                self.current=current

                current=self.head

        
                while current:
                        print(current.data,end=" ")
                        current =current.next
                print("end of List")


        # inserting values in a linked list - in the beginning

        def insert(self,new=None):
                self.new=new
                newNode =Node(new)
                newNode.next=self.head
                self.head=newNode
        
        
        # inserting the values in the end of the linked list
        def insertend(self,new=Node):
                self.new=new
                new = Node(new)
                last_node = self.head
                while(last_node.next):
                        last_node = last_node.next
                last_node.next = new


        # inserting at the given node

        def insert_at_mid(self,data,x):
                self.data = data
                self.x = x

                temp = self.head
                newNode = Node(data)

                while(temp):
                        if (temp.data == x):
                                newNode.next = temp.next
                                temp.next = newNode
                        temp = temp.next # used for next iteration in while loop

        # deleting the values in a linke  list
        
        def delete(self,value):
                temp=self.head
                    # Check if head node itself holds the value to be deleted
                if temp.data == value:
                        self.head =temp.next
                        return

                while temp : # untill temp become None
                        if temp.data == value:
                                break
                        prev = temp
                        temp = temp.next
                if temp != None :
                        prev.next = temp.next
                else:
                        return # if element not found in the list then it will return 

        
        # searching in list

        def search(self,x):
                current =self.head
                while current :
                        if current.data == x :
                                print (x,": found")
                                break
                        current = current.next
                
                if current == None :
                        print(x,": Not found") # search value not found the , this will execute
                
        # sorting in a linked list

        def sort(self):
                temp = self.head
                a = [] # create in built data type List []
                while temp :
                        a.append(temp.data)
                        temp = temp.next
                a.sort()
                new = LinkedList()
                for i in a :
                        new.add(i)
                new.List()
                return new # this will return new sorted linked list


l1 =LinkedList()
l1.add(34)
l1.add(8)
l1.add(4)
l1.add(1)
l1.add(3)
l1.insert(00) # insert at beginning of the list
l1.insertend(99) # insert at end of the list
l1.insert_at_mid(88,1) # insert at given node
l1.List()
l1.delete(1)
l1.List()

l1.search(34) 

l1=l1.sort() # this line initialize new sorted linked list to "l1" object or old unsorted linked list
l1.List() 



# circular linked list 

class Node:
        def __init__(self,data,next=None):
                self.data=data
                self.next = next

class CirLinkedList :
        def __init__(self,head=None):
                self.head=head

        def printList(self,first=None):
                self.first=first

                first=self.head

                while first :
                        print(first.data)
                        if first.next == self.head:
                                break
                        first = first.next


obj = CirLinkedList()

obj.head=Node(5)
second =Node(34)
third=Node(98)

obj.head.next=second
second.next=third
third.next=obj.head

obj.printList()




# doubly linked list


class Node:
        def __init__(self,data,next=None,prev=None):
                self.data = data
                self.next = next
                self.prev = prev


class DoblyList:
        def __init__(self,head=None):
                self.head=head


        def printList(self,first=None):
                self.firts=first
                first=self.head
                while first :
                        print(first.data,end=" ")
                        first=first.next
                print("\n")
        def revPrint(self,last=None): # reverse print of list
                self.last=last
                last = self.head
                while (last.next):
                        last = last.next
                while( last):
                        print(last.data,end=" ")
                        last =last.prev
                
obj = DoblyList()
obj.head=Node(1) # adding data for node 
second=Node(2)
third=Node(3)
fourth=Node(4)


obj.head.next=second   # adding link for the node 
second.next=third
third.next=fourth

second.prev=obj.head  # adding previous link for nodes
third.prev=second
fourth.prev=third


obj.printList()
obj.revPrint()


                


                

                
                