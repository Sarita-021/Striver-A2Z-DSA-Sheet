'''Given a number N. Find its unique prime factors in increasing order.'''
    
class Solution:
    def AllPrimeFactors(self, N):
        res = []
        i = 2
        while i * i <= N:
            if (N%i == 0):
                res.append(i)
                while (N%i == 0):
                    N = N/i
            i += 1
        if N != 1:
            res.append(int(N))
        return res