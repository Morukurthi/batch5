# class happy:
#     a=100
#     def method(self):
#         b=12
#         print(self.a)
#         print(b)
# obj=happy()
# print(obj.a)
# obj.method()


# #encapsulation
# class  encap:
#     _a=10
#     c=20
#     def encapfunction(self):
#         _b=200
#         print("Encap function-accessing protected")
#         print(self._a+10)
# obj=encap()
# print(obj._a)
# obj.encapfunction()
# print(obj.c)
#
# #private
# class encap:
#     __a=10
#     print(__a)
#     def encapfunction(self):
#         print(self.__a)
# obj=encap()
# obj.encapfunction()
# print(obj.__a) # will throw error

#x=200
#print(id(x))

# num=int(input("enter a number:"))
# print(type(num))
# print(num)

#swapping of two numbers
# a=10
# b=20
# print("before swap")
# print("a=",a)
# print("b=",b)
# a=a^b
# b=a^b
# a=a^b
# print("a=",a)

#deleting at given_position
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Singlelinkedlist:
#     def __init__(self):
#         self.head=None
#     def delete_position(self,pos):
#         temp=self.head.next
#         prev=self.head
#         for i in range(1,pos-1):
#             temp=temp.next
#             prev=prev.next
#         prev.next=temp.next
#         temp.next=None
#     def display(self):
#         if self.head is None:
#             print("ll is empty")
#         else:
#             temp=self.head
#             while(temp):
#                 print(temp.data,"==>",end=" ")
#                 temp=temp.next
# obj=Singlelinkedlist()
# n1=Node(100)
# obj.head=n1
# n2=Node(200)
# obj.head.next=n2
# n3=Node(249)
# n2.next=n3
# obj.display()
# print(" ")
# obj.delete_position(2)
# obj.display()

#guessing number
# import random
# n=random.randrange(1,100)
# guess=int(input("enter any number:"))
# while n!=guess:
#     if guess<n:
#         print("too low")
#         guess=int(input("enter number again:"))
#     elif guess>n:
#         print("too high")
#         guess=int(input("enter number again:"))
#     else:
#         break
# print("you guessed it right")

# deletion at lastnode
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Singlelinkedlist:
#     def __init__(self):
#          self.head=None
#     def delete(self):
#          temp=self.head.next
#          prev=self.head
#          while temp.next is not None:
#              temp=temp.next
#              prev=prev.next
#              prev.next=None
#     def display(self):
#             if self.head is None:
#                 print("ll is empty")
#             else:
#                 temp=self.head
#             while(temp):
#                  print(temp.data,"==>",end=" ")
#                  temp=temp.next
# obj=Singlelinkedlist()
# n1=Node(100)
# obj.head=n1
# n2=Node(200)
# obj.head.next=n2
# n3=Node(249)
# n2.next=n3
# obj.display()
# print(" ")
# obj.delete()
# obj.display()

#deletion at firstnode
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Singlelinkedlist:
#     def __init__(self):
#          self.head=None
#     def delete(self):
#          temp=self.head
#          self.head=temp.next
#          temp.next=None
#     def display(self):
#             if self.head is None:
#                 print("ll is empty")
#             else:
#                 temp=self.head
#             while(temp):
#                  print(temp.data,"==>",end=" ")
#                  temp=temp.next
# obj=Singlelinkedlist()
# n1=Node(100)
# obj.head=n1
# n2=Node(200)
# obj.head.next=n2
# n3=Node(249)
# n2.next=n3
# obj.display()
# print(" ")
# obj.delete()
# obj.display()


#inserting a node at beginning

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class singlelinkedlist:
#     def __init__(self):
#         self.head=None
#     def insert_beginning(self,data):
#         nb=Node(data)
#         nb.next=self.head
#         self.head=nb
#     def display(self):
#          if self.head is None:
#              print("ll is empty")
#          else:
#             temp=self.head
#             while(temp):
#                  print(temp.data,"==>",end=" ")
#                  temp=temp.next
# obj=singlelinkedlist()
# n1=Node(100)
# obj.head=n1
# n2=Node(200)
# obj.head.next=n2
# n3=Node(249)
# n2.next=n3
# obj.display()
# print(" ")
# obj.insert_beginning(23)
# obj.display()

#implementation on double linledlist:
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
# class Dll:
#     def __init__(self):
#         self.head=None
#     def display(self):
#         if self.head is None:
#             print("empty")
#         else:
#             temp=self.head
#             while temp:
#                 print(temp.data,"<--->",end=" ")
#                 temp=temp.next
# l=Dll()
# n1=Node(111)
# l.head=n1
# n2=Node(122)
# n2.prev=n1
# n1.next=n2
# l.display()

#insert at begin:
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
# class Dll:
#     def __init__(self):
#         self.head=None
#     def insert_start(self):
#         n=Node(300)
#         temp=self.head
#         temp.prev=n
#         n.next=temp
#         self.head=n
#     def display(self):
#         if self.head is None:
#             print("empty")
#         else:
#             temp=self.head
#             while temp:
#                 print(temp.data,"<--->",end=" ")
#                 temp=temp.next
# l=Dll()
# n1=Node(111)
# l.head=n1
# n2=Node(122)
# n2.prev=n1
# n1.next=n2
# l.insert_start()
# l.display()

#insetion at ending
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
# class Dll:
#     def __init__(self):
#         self.head=None
#     def insert_end(self):
#         n=Node(300)
#         temp=self.head
#         while temp.next is not None:
#             temp=temp.next
#             temp.next=n
#             n.prev=temp
#     def display(self):
#         if self.head is None:
#             print("empty")
#         else:
#             temp=self.head
#             while temp:
#                 print(temp.data,"<--->",end=" ")
#                 temp=temp.next
# l=Dll()
# n1=Node(111)
# l.head=n1
# n2=Node(122)
# n2.prev=n1
# n1.next=n2
# l.insert_end()
# l.display()

#insertion at given position:
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Dll:
    def __init__(self):
        self.head=None
    def insert_pos(self,pos):
        n=Node(300)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n

    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<--->",end=" ")
                temp=temp.next
l=Dll()
n1=Node(111)
l.head=n1
n2=Node(122)
n2.prev=n1
n1.next=n2
l.insert_pos(1)
l.display()
