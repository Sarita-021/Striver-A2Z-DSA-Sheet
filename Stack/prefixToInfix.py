'''You are given a string S of size N that represents the prefix form of a valid mathematical expression. 
The string S contains only lowercase and uppercase alphabets as operands and the operators are +, -, *, /, %, 
and ^.Convert it to its infix form.

'''

class Solution:
    def preToInfix(self, pre_exp):
        # Code here
        stack = []
        for i in range(1,len(pre_exp)+1):
            if pre_exp[-i].isalnum():
                stack.append(pre_exp[-i])
            elif pre_exp[-i] in '+-*%/^':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append('('+v1+pre_exp[-i]+v2+')')
        return stack[0]
        