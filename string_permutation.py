#A permutation also called an "arrangement number" or "order," 
# is a rearrangement of the elements of an ordered 
# list S into a one-to-one correspondence with S itself




S=input()
arr=[]
for element in S:
    arr.append(element)
arr.sorted()
n=len(arr)
sum=""
arr1=[]
for i in range(n):
    sum=sum+arr[i]
    arr1.append(sum)