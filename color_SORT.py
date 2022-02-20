n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
for i in range(len(arr)):
    print(arr[i])

#red, o
#white, 1 
# and blue. 2 
#object with same color are put similar place

'''for i in range(n):
    if (arr[i]>arr[i+1]):
        arr[i],arr[i+1] = arr[i+1],arr[i]'''


