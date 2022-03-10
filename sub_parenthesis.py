def findMaxLen(s):
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
                
        return maxlength

s="()(())("
print(findMaxLen(s))