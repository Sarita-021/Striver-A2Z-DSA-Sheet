'''Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer 
after removing k digits from num.
https://leetcode.com/problems/remove-k-digits/description/ '''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If k > 0, remove remaining k digits from the end of the stack
        stack = stack[:-k] if k > 0 else stack
        
        # Remove leading zeros
        result = ''.join(stack).lstrip('0')
        
        # Handle edge case where result might be empty
        return result if result else '0'  