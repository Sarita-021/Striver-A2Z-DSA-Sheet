'''Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.'''

from typing import List


def timeTaken(piles, n) :
    tt = 0
    for i in range(len(piles)):
        tt += ceil(piles[i]/n)
    return tt

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high
        while low <= high :
            mid = (low+high)//2
            totalHr = timeTaken(piles, mid)
            if totalHr > h:
                low = mid+1
            else :
                res = mid
                high = mid-1
        return res