
def linearSearch(arr,N):
    for i in range(len(arr)):
        if arr[i]==n:
            print("Found",N,"at location",i)
        
    return i
n=int(input())
arr=[]

while (n>0):
    arr.append(int(input()))
    n=n-1
N=int(input())
print(linearSearch(arr,N))