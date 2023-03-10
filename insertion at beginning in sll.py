class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
         if self.head is None:
             print("ll is empty")
         else:
            temp=self.head
            while(temp):
                 print(temp.data,"==>",end=" ")
                 temp=temp.next
obj=singlelinkedlist()
n1=Node(100)
obj.head=n1
n2=Node(200)
obj.head.next=n2
n3=Node(249)
n2.next=n3
obj.display()
print(" ")
obj.insert_beginning(23)
obj.display()
