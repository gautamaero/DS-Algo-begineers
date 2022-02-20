def rotate_array_clockwise(arr1):
    arr2=[]
    #c=[]
    #d=[]
    #arr3=[]
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

        




    '''for i in range(len(arr2)):
        for j in range(len(arr2[0])-1,-1,-1):
            d.append(arr2[i][j])

        arr3.append(d)'''

    return arr2
n=int(input())
m=int(input()) # No of rotation to be performed
arr1=[]
for i in range(n):
    a=list(map(int,input().split()[:n]))
    arr1.append(a)
print(arr1,rotate_array_clockwise(arr1))



'''for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(a[i][j],end=" ")
    print() '''


#00,01,02
#[[1,2,3],
# [11,12,13]]
#10,11,12,13

