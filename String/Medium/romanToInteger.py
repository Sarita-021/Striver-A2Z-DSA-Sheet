'''Given a roman numeral, convert it to an integer.'''

class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s)-1):
            if m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        ans += m[s[-1]] 
        return ans 