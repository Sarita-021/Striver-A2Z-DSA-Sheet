'''A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid 
if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. 
locked is a binary string consisting only of '0's and '1's. For each index i of locked,

If locked[i] is '1', you cannot change s[i].
But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false.

https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/'''

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False  # Odd-length strings cannot be valid
        
        # Left-to-right check
        min_bal, max_bal = 0, 0
        for i in range(n):
            if locked[i] == '1':
                if s[i] == '(':
                    min_bal += 1
                    max_bal += 1
                else:  # s[i] == ')'
                    min_bal -= 1
                    max_bal -= 1
            else:  # locked[i] == '0', flexible
                min_bal -= 1
                max_bal += 1
            
            if max_bal < 0:
                return False  # Too many closing parentheses
            min_bal = max(min_bal, 0)  # Balance cannot go negative
        
        # Right-to-left check
        min_bal, max_bal = 0, 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '1':
                if s[i] == ')':
                    min_bal += 1
                    max_bal += 1
                else:  # s[i] == '('
                    min_bal -= 1
                    max_bal -= 1
            else:  # locked[i] == '0', flexible
                min_bal -= 1
                max_bal += 1
            
            if max_bal < 0:
                return False  # Too many opening parentheses
            min_bal = max(min_bal, 0)  # Balance cannot go negative
        
        return min_bal == 0
