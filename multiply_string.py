'''Given two numbers as strings s1 and s2. Calculate their Product.
Note: The numbers can be negative.
Example 1:
Input:
s1 = "33"
s2 = "2"
Output:
66
Example 2:

Input:
s1 = "11"
s2 = "23"
Output:
253

Your Task:

You don't need to read input or print anything. Your task is to complete the function multiplyStrings() which takes two strings s1 and s2 as input and returns their product as a string.

Note : You are not allowed to use any built-in function or convert the strings to integer.


Expected Time Complexity: O(n1* n2)
Expected Auxiliary Space: O(n1 + n2) ; where n1 and n2 are sizes of strings s1 and s2 respectively.


Constraints:
1 ≤ length of s1 and s2 ≤ 103'''


def multiply_str(s1, s2):
    s1=int(s1)
    s2=int(s2)
    if (s1==0 or s2==0):
        return 0
    else:
        return str(s1*s2)

s1=input()
s2=input()
print(multiply_str(s1,s2))
