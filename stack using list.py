stack=[]
def push():
    element=int(input("enter the element:"))
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
    print("removed element:",e)
    print(stack)
while True:
    print("select operation 1.push 2.po 3.quit")
    choice=int(input("enter choice"))
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("enter the correct operation")
