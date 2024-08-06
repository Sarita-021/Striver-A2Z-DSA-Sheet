'''After processing the entire string, return the modified string s which has the outermost parentheses removed 
from each primitive valid parentheses substring. A valid parentheses string s is primitive if it is nonempty, and
there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.'''


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c1 = c2 = i = 0
        while i < len(s):
            if s[i] == "(" :
                c1 += 1
            else :
                c2 += 1
            if c1 == 1 and c2 == 0:
                s = s[:i] + s[i+1:]
            elif c1 == c2 :
                s = s[:i] + s[i+1:]
                c1, c2 = 0,0
            else :
                i += 1
        return s
        