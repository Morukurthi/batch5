class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Dll:
    def __init__(self):
        self.head=None
    def insert_start(self):
        n=Node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
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
l.insert_start()
l.display()
