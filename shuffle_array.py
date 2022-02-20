from re import A


n=int(input())
arr1=[]
for i in range(2*n):
    arr1.append(int(input()))

for i in range(n):
    #for j in range(n,2*n):
    arr1[i],arr1[-i-1]=arr1[-i-1],arr1[i]   

         
print(arr1)


#while (n>0):
#    arr1.append(int(input()))
#    n=n-1
#print(arr1)

