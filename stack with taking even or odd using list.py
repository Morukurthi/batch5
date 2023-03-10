stack1=[]
stack2=[]
def push():
    for i in range(5):
        element=int(input("enter the element:"))
        if (element%2==0):
            stack1.append(element)
        else:
            stack2.append(element)
def pop_element():
    pop_what=input("1 or 2")
    if pop_what=="1":
        if not stack1:
            print("stack is empty")
        else:
            e=stack1.pop()
            print("removed element:",e)
            print(stack1)
    else:
        if not stack2:
            print("stack is empty")
        else:
            e = stack2.pop()
            print("removed element:", e)
            print(stack2)
def display():
    what=input("1 or 2")
    if what=="1":
        print(stack1)
    else:
        print(stack2)
while True:
    print("select operation 1.push 2.pop 3.display 4.quit")
    choice=int(input("enter choice"))
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("enter the correct operation")
