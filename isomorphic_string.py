'''Given two strings 'str1' and 'str2', 
check if these two strings are isomorphic to each other.
Two strings str1 and str2 are called isomorphic if 
there is a one to one mapping possible for every character of str1 to every character of str2 while preserving the order.
Note: All occurrences of every character in ‘str1’ should map 
to the same character in ‘str2’'''

'''Input:
str1 = aab
str2 = xxy
Output: 1
Explanation: There are two different
charactersin aab and xxy, i.e a and b
with frequency 2and 1 respectively.
Example 2:Input:
str1 = aab
str2 = xyz
Output: 0
Explanation: There are two different
charactersin aab but there are three
different charactersin xyz. So there
won't be one to one mapping between
str1 and str2.'''


from tkinter import N


str1=input()
str2=input()
arr1=[]
arr2=[]
for elemen in str1:
    arr1.append(elemen)
for elemen in str2:
    arr2.append(elemen)
n1=len(arr1)
n2=len(arr2)
arr1=sorted(arr1)
arr2=sorted(arr2)
count=1
if(n1==n2):
    if 
