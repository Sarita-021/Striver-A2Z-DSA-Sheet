'''A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are 
prime (2, 3, 5, or 7).
For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at o
dd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.

https://leetcode.com/problems/count-good-numbers/description/

Total Good Numbers:
° If n is even, the total number of good numbers is 5^(n/2) * 4^(n/2) = 20^(n/2)
° If n is odd, the total number of good numbers is 5 * 20^((n-1)/2).
x^n = x^(2*(n/2)) = x^(n/2) * x^(n/2)
'''

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        def expo(x: int, num: int) -> int:
            if num == 0:
                return 1  
            elif num & 1 == 0:
                return expo((x * x) % MOD, num // 2)
            return x * expo(x, num - 1) % MOD

        return 5 ** (n % 2) * expo(20, n // 2) % MOD