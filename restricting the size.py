n=int(input("enter size:"))
a=list(map(int,input().split(','))) [n:]
total=0
for i in a:
    #print(i,end=' ')
    total=total+i
print(total)
