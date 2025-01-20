'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.'''

from typing import List

def median(a,b):
    n1, n2 = len(a), len(b)
    if n1 > n2:
        return median(b, a)

    n = n1 + n2  
    left = (n1 + n2 + 1) // 2 
    low, high = 0, n1
    while (low <= high):
        mid1 = (low + high) // 2
        mid2 = left - mid1

        l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
        if mid1-1 >= 0 :
            l1 = a[mid1-1]
        if mid2 - 1 >= 0:
            l2 = b[mid2 - 1]
        if mid1 < n1 :
            r1 = a[mid1]
        if mid2 < n2 :
            r2 = b[mid2]
        
        if l1 <= r2 and l2 <= r1:
            if n%2 == 0 :
                return (max(l1,l2) + min(r1,r2))/2
            else :
                return max(l1,l2)
        elif l1 > r2 :
            high = mid1-1
        else :
            low = mid1+1

    return 0
 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(nums1,nums2)