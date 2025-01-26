'''Given an infix expression in the form of string s. Convert this infix expression to a postfix expression.

Infix expression: The expression of the form a op b. When an operator is in between every pair of operands.
Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. Ignore the right associativity of ^.'''


def priority(op):
    if op == '(':
        return 0
    elif op in '+-':
        return 1
    elif op in '*/':
        return 2
    elif op in '^':
        return 3

class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, s):
        res = []
        stack = []
        for c in s:
            if c.isalnum():
                res.append(c)
            elif c == '(':
                stack.append(c)
            elif c == ')':
                while stack[-1] != '(':
                    res.append(stack.pop())
                stack.pop()
            else:
                if not stack or priority(stack[-1]) < priority(c):
                    stack.append(c)
                else:
                    while stack and priority(stack[-1]) >= priority(c):
                        i = stack.pop()
                        res.append(i)
                    stack.append(c)
                    
        while stack:
            i = stack.pop()
            res.append(i)
                
        return ''.join(res)

