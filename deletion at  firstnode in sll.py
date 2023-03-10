class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singlelinkedlist:
    def __init__(self):
         self.head=None
    def delete(self):
         temp=self.head
         self.head=temp.next
         temp.next=None
    def display(self):
            if self.head is None:
                print("ll is empty")
            else:
                temp=self.head
            while(temp):
                 print(temp.data,"==>",end=" ")
                 temp=temp.next
obj=Singlelinkedlist()
n1=Node(100)
obj.head=n1
n2=Node(200)
obj.head.next=n2
n3=Node(249)
n2.next=n3
obj.display()
print(" ")
obj.delete()
obj.display()
