'''You are given an integer array bloomDay, an integer m and an integer k.
You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used 
in exactly one bouquet. Return the minimum number of days you need to wait to be able to make m bouquets
from the garden. If it is impossible to make m bouquets return -1.'''

from typing import List


def cntBqe(bloomDay, n, af) :
    cnt = 0
    bcnt = 0
    for i in range(len(bloomDay)):
        if bloomDay[i] <= n :
            cnt += 1
        else :
            cnt = 0
        
        if cnt == af :
            bcnt += 1
            cnt = 0

    return bcnt

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low, high = min(bloomDay), max(bloomDay)
        ans = -1
        if m*k > len(bloomDay) :
            return -1
        while low <= high :
            mid = (low+high)//2
            tbcnt = cntBqe(bloomDay, mid, k)
            if tbcnt < m :
                low = mid+1
            else :
                high = mid-1
        return low