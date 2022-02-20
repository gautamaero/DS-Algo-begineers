def square_matrix_input(m):
    arr1=[]
    for i in range(m):
        arr=list(map(int,input().split()[:m]))
        arr.sort()
        arr1.append(arr)
    #print(type(arr1))
	#arr1.sort()
    
    for i in range(len(arr1)):# traversing through the rows
        for j in range(len(arr1[0])): # Findign the number of columns
            if (i==j):
                if (arr1[i][j]<0):
                    #print(arr1[i][j])
                    arr1[i][j]=0
                    #arr1=arr1.insert(arr1[i][j],0)
            #arr1.insert(index,'yellow')
                elif (arr1[i][j]>=0):
                    #print(arr1[i][j])
                    arr1[i][j]=1
                    #arr1=arr1.insert(arr1[i][j],1)
        
    return arr1
m=int(input())
print(square_matrix_input(m))