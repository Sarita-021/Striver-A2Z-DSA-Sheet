'''You are given a positive number N. Using the concept of Sieve, compute its prime factorisation.
https://www.geeksforgeeks.org/problems/prime-factorization-using-sieve/1?'''

class Solution:
    def __init__(self, limit=10**6):  # Default limit (can be changed)
        self.limit = limit
        self.spf = list(range(limit + 1))  # Initialize each number as its own smallest factor
        self.sieve() 
        
    def sieve(self):
        for i in range(2, int(self.limit**0.5) + 1):
            if self.spf[i] == i:  # If `i` is prime
                for j in range(i * i, self.limit + 1, i):  # Mark multiples of `i`
                    if self.spf[j] == j:  # Update only if `spf[j]` is not set
                        self.spf[j] = i
        
    def findPrimeFactors(self, N):
        factors = []
        while N > 1:
            factors.append(self.spf[N])  # Get the smallest prime factor
            N //= self.spf[N]  # Reduce n by dividing by its smallest prime factor
        return factors