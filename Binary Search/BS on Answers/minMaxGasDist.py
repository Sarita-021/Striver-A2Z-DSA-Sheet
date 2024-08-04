'''You are given a sorted array "arr" of length "n", which contains positive integer positions of "n" gas 
stations on the X-axis. You are also given an integer "k". You have to place "k" new gas stations on the X-axis.
You can place them anywhere on the non-negative side of the X-axis, even on non-integer positions. Let "dist" be 
the maximum value of the distance between adjacent gas stations after adding k new gas stations.
Find the minimum value of "dist".'''

from typing import List

def numberOfGasStationsRequired(dist, arr):
    n = len(arr)  # size of the array
    cnt = 0
    for i in range(1, n):
        numberInBetween = ((arr[i] - arr[i - 1]) / dist)
        if (arr[i] - arr[i - 1]) == (dist * numberInBetween):
            numberInBetween -= 1
        cnt += numberInBetween
    return cnt


def minimiseMaxDistance(arr, k):
    n = len(arr)  # size of the array
    low = 0
    high = 0

    # Find the maximum distance:
    for i in range(n - 1):
        high = max(high, arr[i + 1] - arr[i])

    # Apply Binary search:
    diff = 1e-6
    while high - low > diff:
        mid = (low + high) / 2.0
        cnt = numberOfGasStationsRequired(mid, arr)
        if cnt > k:
            low = mid
        else:
            high = mid

    return high

class Solution:
    def findMinDist(self, nums: List[int], k) -> float:
        return minimiseMaxDistance(nums, k)