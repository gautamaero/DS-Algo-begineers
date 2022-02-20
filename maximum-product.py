
'''n=int(input())
arr=[]
while (n>0):
    arr.append(int(input()))
    n=n-1
for i in range(0, len(arr)-1):
    product=arr[i]*arr[i+1]
    arr1.append(product)

print(max(arr1))    '''




def max_product(arr):
    arr1=[]
    for i in range(0, len(arr)-1):
        arr1.append(arr[i]*arr[i+1])

    return max(arr1)

n=int(input())
arr=[]
while (n>0):
    arr.append(int(input()))
    n=n-1

print(max_product(arr))



