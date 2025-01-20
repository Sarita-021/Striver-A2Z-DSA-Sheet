'''You are given 2 numbers (n , m); the task is to find n√m (nth root of m).'''

def NthRoot(self, n, m):
    if m == 1:
        return 1
    if n == 1:
        return m
    low = 1
    high = (m//n)+1
    while low <= high :
        mid = (low+high)//2
        if mid**n == m:
            return mid
        elif mid**n < m:
            low = mid+1
        else :
            high = mid-1
    return -1