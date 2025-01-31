'''Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)

https://leetcode.com/problems/string-to-integer-atoi/description/ '''

def recursive(s, i, num):
    if i >= len(s) or not s[i].isdigit():
        return num
    num = num * 10 + int(s[i])
    return recursive(s, i + 1, num)

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        
        sign = -1 if s[0] == '-' else 1
        if s[0] in '-+':
            s = s[1:]

        ans = recursive(s, 0, 0)
        ans = sign * ans
        return max(min(ans, 2**31 - 1), -2**31)
    
    
# Iterative solution 

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        
        sign = -1 if s[0] == '-' else 1
        if s[0] in '-+':
            s = s[1:]
        
        num = 0
        for char in s:
            if not char.isdigit():
                break
            num = num * 10 + int(char)
        
        ans = sign * num
        return max(min(ans, 2**31 - 1), -2**31)