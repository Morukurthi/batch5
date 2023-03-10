class CircularQueue():
    def __init__(self,size):
        #intializing the class
        self.size=size
        #can  use self.queue=[None]*size
        self.queue =[None for i in range(size)]
        self.front=self.rear=-1
    def enqueue(self,data):
        #condition if queue is full
        if ((self.rear+1) % self.size==self.front): #size 6 index from 0
            print("queue is full\n")
        #condition for empty queue
        elif (self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
            #always add element at tail place
        else:
            #next postion of rear
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
    def dequeue(self):
        if (self.front==-1):
            #condition if queue is empty
            print("queue is empty")
        # condition for only one element
        elif (self.front==self.rear):
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1) %self.size
            return temp
    def display(self):
        if self.front==-1:
            print("queue is empty")
        elif (self.rear>=self.front):
            print("elements in the circular queue",end=" ")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
                print()
        else:
            print("elements in circular queue",end=" ")
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        if((self.rear+1)% self.size==self.front):
            print("queue is full")
ob=CircularQueue(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-2)
ob.display()
print("removed element",ob.dequeue())
print("removed element",ob.dequeue())
ob.display()
ob.enqueue(23)
ob.enqueue(34)
ob.display()
