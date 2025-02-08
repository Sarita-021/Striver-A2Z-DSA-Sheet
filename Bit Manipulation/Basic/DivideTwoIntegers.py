'''Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be 
truncated to 8, and -2.7335 would be truncated to -2.
Return the quotient after dividing dividend by divisor.
https://leetcode.com/problems/divide-two-integers/description/'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Determine the sign of the result
        is_negative = (dividend < 0) ^ (divisor < 0)  # XOR to check if signs differ
        
        # Work with absolute values
        abs_dividend, abs_divisor = abs(dividend), abs(divisor)
        result = 0
        
        # Perform division using bit manipulation
        while abs_dividend >= abs_divisor:
            temp_divisor, multiple = abs_divisor, 1
            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            abs_dividend -= temp_divisor
            result += multiple
        
        # Apply the sign
        return -result if is_negative else result