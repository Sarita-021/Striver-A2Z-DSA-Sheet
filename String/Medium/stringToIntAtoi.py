'''Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
The algorithm for myAtoi(string s) is as follows:

1. Whitespace: Ignore any leading whitespace (" ").
2. Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the 
    string is reached. If no digits were read, then the result is 0.
4. Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to 
    remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 
    231 - 1 should be rounded to 231 - 1.

Return the integer as the final result.'''


class Solution:
    def myAtoi(self, s: str) -> int:
        int_max, int_min = (2**31) - 1, -1 * (2**31)
        ans = 0
        m = 1
        for i in range(len(s)):
            if s[:i+1].isspace() : 
                continue
            elif s[i] in "0123456789" :
                ans = ans*10 + int(s[i])
            elif s[i] == "-" and (s[:i].isspace() or i == 0):
                    m = -1
            elif s[i] == "+" and (s[:i].isspace() or i == 0) :
                continue
            else :
                print("hi", s[i])
                break
        if m == -1:
            return min(max(-ans, int_min), int_max)
        return min(max(ans, int_min), int_max)