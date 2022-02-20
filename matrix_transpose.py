def transpose_matrix(arr1):
    arr2=[]
    for i in range(len(arr1)):
        c=[]
        for j in range(len(arr1[0])):
            c.append(arr1[j][i])
        #arr2.append(arr1[i][j])
        arr2.append(c)
    
    for i in range(len(arr2)):
        for j in range(len(arr2[0])):
            print(arr2[i][j],end=" ")
        print()

m=int(input()) #row 
#n=int(input()) # col

arr1=[]
for i in range(m):
    a=list(map(int,input().split()))
    arr1.append(a)
#print('main-matrix',arr1)
print(transpose_matrix(arr1))

