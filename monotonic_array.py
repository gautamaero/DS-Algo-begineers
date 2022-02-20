N=int(input())
arr=[]
arr1=[]
while(N>0):
    arr.append(int(input()))
    N=N-1

if (len(arr)==0):
    print('False')
else:
    for i in range(len(arr)-1):
        if (arr[i+1]>=arr[i]):
            arr1.append('True')
#print(len(arr1),len(arr))
    if (len(arr1)==len(arr)-1):
        print('True')
    else:
        print('False')

