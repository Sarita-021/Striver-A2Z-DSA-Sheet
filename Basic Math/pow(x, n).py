'''Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
https://takeuforward.org/data-structure/implement-powxn-x-raised-to-the-power-n/ '''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        nn = n
        if nn < 0:
            nn = -1 * nn
        while nn:
            if nn % 2:
                ans = ans * x
                print(ans)
                nn = nn - 1
            else:
                x = x * x
                nn = nn // 2
        if n < 0:
            ans = 1.0 / ans
        return ans