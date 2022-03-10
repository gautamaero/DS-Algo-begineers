'''Given two stringsaandbconsisting of lowercase characters.
The task is to check whether two given strings are an anagram of each other
or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. 
For example, act and tac are an anagram of each other.

Example 1:

Input:a = geeksforgeeks, b = forgeeksgeeks
Output: YES
Explanation: Both the string have samecharacters with
        same frequency. So, both are anagrams.
Example 2:

Input:a = allergy, b = allergic
Output: NO
Explanation:Characters in both the strings are 
        not same, so they are not anagrams.'''

#anagram meaning =शब्द बदलकर कर नया शब्द बनाना
'''def anagram(a,b):
    n1=len(a)
    n2=len(b)
    arr1=[]
    arr2=[]
    if(n1==n2):
        for element in a:
            arr1.append(element)
        for element in b:
            arr2.append(element)

        #for i in range(len(arr1)):
        for element1 in arr1:
            #print(element)
            for element2 in arr2:
            #for j in range(len(arr2)):
                #print(arr2[j])
                if(element1==element2):
                    return 'YES'
                else:
                    return 'NO' '''

#a=input()
#geeksforgeeks
#b=input()
#forgeeksgeeks
a='geeksforgeeks'
b='forgeeksgeeks'
#print(anagram(a,b))


#a=input()
#b=input()
def anagram(a,b):
    arr1=[]
    arr2=[]
    for element in a:
        arr1.append(element)
    for element in b:
        arr2.append(element)
    n1=len(arr1)
    n2=len(arr2)
    arr1=sorted(arr1)
    arr2=sorted(arr2)
    if (n1==n2):
        for i in range(len(arr1)):
            if(arr1[i]==arr2[i]):
                return 1
            else:
                return 0
    else:
        return 0

a=input()
b=input()
print(anagram(a,b))

