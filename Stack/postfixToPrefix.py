'''You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its prefix form.'''


class Solution:
    def postToPre(self, post_exp):
        stack = []
        for i in range(len(post_exp)):
            if post_exp[i].isalnum():
                stack.append(post_exp[i])
            elif post_exp[i] in '+-*%/^':
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(post_exp[i]+v1+v2)
        return stack[0]