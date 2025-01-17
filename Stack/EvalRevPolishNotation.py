'''You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.'''


from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                    continue
                case '*':
                    stack.append(stack.pop() * stack.pop())
                    continue
                case '-':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                    continue
                case '/':
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b/a))
                    continue
                case _:
                    stack.append(int(token))
        return stack.pop()