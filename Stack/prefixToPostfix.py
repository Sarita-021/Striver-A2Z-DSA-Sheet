'''You are given a string that represents the prefix form of a valid mathematical expression. Convert it to its postfix form.'''

class Solution:
    def preToPost(self, pre_exp):
        stack = []
        for i in range(1,len(pre_exp)+1):
            if pre_exp[-i].isalnum():
                stack.append(pre_exp[-i])
            elif pre_exp[-i] in '+-*%/^':
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v1+v2+pre_exp[-i])
        return stack[0]