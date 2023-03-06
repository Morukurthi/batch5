# class happy:
#     a=100
#     def method(self):
#         b=12
#         print(self.a)
#         print(b)
# obj=happy()
# print(obj.a)
# obj.method()
#
#
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

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def display(self):
          if self.head is None:
             print("ll is empty")
          else:
            temp = self.head
            while (temp):
                print(temp.data, "==>", end=" ")
                temp = temp.next
# obj = SLL()
# n1 = Node(100)
# obj.head = n1
# n2 = Node(200)
# obj.head.next = n2
# n3 = Node(300)
# n2.next = n3
# obj.display()
#

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_beginning(selfself,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
     def display(self):
         if self.head is none:
             print("ll is empty")
         else:
