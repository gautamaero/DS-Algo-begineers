n=int(input())
A=[]
P=int(input())
if (n>2):
    while (n>0):
        A.append(int(input()))
        n=n-1
counter=0
for i in range(len(A)):
    if (A[i]>P):
        counter+=1
if (counter>=1):
    print(counter)
elif (counter<1):
    print(-1)
