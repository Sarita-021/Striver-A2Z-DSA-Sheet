'''A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with
packages on the conveyor belt (in the order given by weights). We may not load more weight than
the maximum weight capacity of the ship.'''

from typing import List


def maxCap(weights):
    cap = 0
    for i in range(len(weights)):
        cap += weights[i]
    return cap

def daysTaken(weights, cap):
    cnt = 0
    days = 1
    for i in range(len(weights)):
        cnt += weights[i]
        if cnt > cap :
            days += 1
            cnt = weights[i]
    return days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = maxCap(weights)
        ans = low
        while low <= high :
            mid = (low+high)//2
            d = daysTaken(weights, mid)
            if d > days :
                low = mid+1
            elif d <= days :
                ans = mid
                high = mid-1
        return ans