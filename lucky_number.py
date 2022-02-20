'''def luckyNumber(arr):
    arr.sort
    counter=1
    for i in range(len(arr)):
        if (arr[i]==arr[i-1]):
            counter+=1
            if (counter==arr[i-1]):
                print(arr[i])
            else:
                print(-1)
n=int(input())
arr=[]
while(n>0):
    arr.append(int(input()))
    n=n-1
print(luckyNumber(arr))'''


def luckyNumber(arr):
    for i in range(len(arr)):
        if (arr.count(arr[i])==arr[i]):
            print(arr[i])
            break
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
luckyNumber(arr)






'''class Node:

    # Function to initialize the node object
    def __init__(self,data):
        self.data=data #Assign data to the node
        self.next=None  # Initialises next element as null

class LinkedList:
    #This is used to initialize the linked list
    # List object

    def __init__(self):
        self.head=None # Initialize head element as null
        '''