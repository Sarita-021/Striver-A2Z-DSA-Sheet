'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in brackets.values():
                stack.append(c)
            elif c in brackets.keys():
                if not stack or brackets[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return not stack