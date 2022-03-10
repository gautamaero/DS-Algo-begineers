'''Given a string S consisting only of opening and closing parenthesis 'ie '('  and ')', find out the length of the longest valid(well-formed) parentheses substring.
NOTE: Length of the smallest valid substring ( ) is 2.

Example 1:

Input: S = "(()("
Output: 2
Explanation: The longest valid 
substring is "()". Length = 2.
Example 2:

Input: S = "()(())("
Output: 6
Explanation: The longest valid 
substring is "()(())". Length = 6'''

import time
import os
'''def findMaxLen(S):
    # String S consist of only round () parenthesis
    arr=[]
    count=1
    for element in S:
        print('f_check',element)
        time.sleep(2.5)
        if element in ['(',')']:
            time.sleep(2.5)
            #check whether array has contained only opening or any other parenthesis also
            arr.append(element)
        else:
            if not arr:
                return False
            current_element = arr.pop()
            if (current_element=='('):
                if(element==')'):
                    count+=1
                    return count
            if (current_element==')'):
                if(element=='('):
                    count+=1
                    return count'''

'''def findMaxLen(ob, s):
        n = len(s)

        # Variables for left and right counter.
        # maxlength to store the maximum length found so far
        left = right = maxlength = 0

        # Iterating the string from left to right
        for i in range(n):
            # If "(" is encountered,
            # then left counter is incremented
            # else right counter is incremented
            if s[i] == '(':
                left += 1
            else:
                right += 1

            # Whenever left is equal to right, it signifies
            # that the subsequence is valid and
            if (left == right):
                maxlength = max(maxlength, 2 * right)

            # Reseting the counters when the subsequence
            # becomes invalid
            elif (right > left):
                left = right = 0

        left = right = 0

        # Iterating the string from right to left
        for i in range(n-1,-1,-1):

            # If "(" is encountered,
            # then left counter is incremented
            # else right counter is incremented
            if s[i] == '(':
                left += 1
            else:
                right += 1

            # Whenever left is equal to right, it signifies
            # that the subsequence is valid and
            if (left == right):
                maxlength = max(maxlength, 2 * left)

            # Reseting the counters when the subsequence
            # becomes invalid
            elif (left > right):
                left = right = 0
                
        return maxlength'''



def findMaxLen(S):
    arr=[]
    count_left=0
    count_right=0
    #Line 101 to 106 is just to filter only required parenthesis is been inserted by user
    for element in S:
        if element in ['(',')']:
            arr.append(element)
            

    #Now traversing array from the left to right 
    n=len(arr)
    maxlength=0
    for i in range(len(arr)):
        if(arr[i] =='('):
            count_left+=1
        elif(arr[i] ==')'):
            count_right+=1

        if(count_left==count_right):
            maxlength=max(maxlength,2*count_left)

        elif(count_left<count_right):
            count_left=count_right=0

    count_left=count_right=0

    #Now traversing opposite direction of array
    
    for i in range(n-1,-1,-1):

        if(arr[i] =='('):
            count_left+=1
        elif(arr[i] ==')'):
            count_right+=1
        
        if(count_left==count_right):
            maxlength = max(maxlength, 2 *count_right)

        elif(count_left>count_right):
            count_left=count_right=0

    return maxlength

S=")("
print(findMaxLen(S))