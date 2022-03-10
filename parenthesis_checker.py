'''Given an expression string x. Examine whether the pairs
 and the orders of “{“,”}”,”(“,”)”,”[“,”]” 
are correct in exp.For example, the function should return 'true' 
for exp = “[()]{}{[()()]()}” and 'false' for exp = “[(])”.'''


'''Example 1:
Input:
{([])}
Output: 
true
Explanation: 
{ ( [ ] ) }. Same colored brackets can form 
balaced pairs, with 0 number of 
unbalanced bracket.'''

'''Example 2:
Input: 
()
Output: 
true
Explanation: 
(). Same bracket can form balanced pairs, 
and here only 1 type of bracket is 
present and in balanced way.'''

'''Example 3:
Input: 
([]
Output: 
false
Explanation: 
([]. Here square bracket is balanced but 
the small bracket is not balanced and 
Hence , the output will be unbalanced.'''

'''Your Task:
This is a function problem. You only need to complete the function ispar() 
that takes a string as a parameter and returns a boolean value true 
if brackets are balanced else returns false. 
The printing is done automatically by the driver code.'''

#Approach 1

def parenthesis_check(x):
    count1=0
    count2=0
    count3=0
    for element in x:
        print(element)
        if (element=='(' or element==')'):
            count1+=1
            print(count1) 
        elif (element=='{' or element=='}'):
            count2+=1
            print(count2)
        elif (element=='[' or element==']'):
            count3+=1
            print(count3) 

    if (count1%2==0 ):
        return True
    elif (count2%2==0):
        return True
    elif (count3%2==0):
        return True
    else:
        return False
x=input("Enter the parenthesis(as string) sequence to be checked:")
print(parenthesis_check(x))
#Approach 2

'''def parenthesis_check(x):
    arr=[]
    for element in x:
        #arr.append(element) # if we simply use append then empty will
        #also be counted as string and made input so its recomended to check
        
        # first checking open parenthesis
        if (element=='(' or element=='{' or element=='['):
            #if element in ['(','{','[']: line 80 and 81 are same but differnet way of element
            #This if condition will remove extra empty elements or strings
            #as well as closing bracket
            arr.append(element)
        else:
            if not arr:
                return False
        current_element=arr.pop() # This will give last elment of array for finding its closing pair
        if(current_element=='['):
                if(element!=']'): # checking its opposte pair
                    return False 
        if(current_element=='('):
            if (element!=')'):
                return False
        if(current_element=='{'):
            if (element!='}'):
                return False

    if arr:
        return False
    else:
        return True

'''
'''def areBracketsBalanced(expr):
    stack = []

    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:

            # Push the element in the stack
            stack.append(char)
        else:

            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack: # This line not clear
                return False
            current_char = stack.pop()# accessing element
            if current_char == '(':
                if char != ")":
                    return False
            
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    # Check Empty Stack
    if stack:
        return False
    return True

expr=input()
print(areBracketsBalanced(expr)) '''

#x=input("Enter the parenthesis(as string) sequence to be checked:")
#print(parenthesis_check(x))

