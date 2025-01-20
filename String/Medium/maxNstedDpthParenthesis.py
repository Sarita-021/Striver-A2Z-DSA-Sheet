'''Given a valid parentheses string s, return the nesting depth of s. 
The nesting depth is the maximum number of nested parentheses.'''


class Solution:
    def maxDepth(self, s: str) -> int:
        mxD = 0
        ans = 0
        for i in s:
            if i == '(' :
                mxD += 1
            elif i == ')' :
                mxD -= 1
            ans = max(ans, mxD)
        return ans