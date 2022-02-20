n=int(input())
arr=list(map(int,input().split()[:n]))
arr.sort()
strength=0;

def strength(arr):
    for i in range(len(arr)):
        strength +=arr[i]
    return strength
sum=0
for i in range(len(arr)):
    sum=sum+arr[i]+arr[i+1]
    






#if(link_size>=1 and link_size<=len(arr))

    
#arr=[3,-4,5,6,10,-6,-16,18,3,-1]
#sum=0;
#for i in range(len(arr)):
#    sum=sum+arr[i]
#    print(sum)
#print(sum)

