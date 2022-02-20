n=int(input())
arr=list(map(int, input().split()[:n]))
print(arr)
'''while(n>0):
    arr.append(int(input()))
    n=n-1
arr1=[]
arr2=[]
for i in range(len(arr)):
    diff=arr[i]-arr[i-1]
    arr1.append(diff)

    print('first',diff)

for i in range(len(arr)-1):
    diff=arr[i]-arr[i+1]
    arr2.append(diff)
    print('second',diff) '''



