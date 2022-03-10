'''Given an array numbers[] of N positive integers and a 
positive integer X, The task is to find the number of
 ways that X can be obtained by writing pair of integers 
 in the array numbers[] next to each other. In other words, 
 find the number of ordered pairs (i,j) such that i != j and 
 X is the concatenation of numbers[i] and numbers[j]'''

 # Input and output format 

'''Input:
N = 4 
numbers[] = {1, 212, 12, 12}
X = 1212
Output:
3
Explanation:
We can obtain X=1212 by concatenating:
numbers[0] = 1 with numbers[1] = 212
numbers[2] = 12 with numbers[3] = 12
numbers[3] = 12 with numbers[2] = 12'''
def integer_to_string(arr):
    arr=[str(int) for int in arr]
    word=""
    for i in arr:
        word=word+i 

    return word

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print(integer_to_string(arr))
