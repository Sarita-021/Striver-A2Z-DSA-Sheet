'''Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.'''


from cmath import inf
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        preProd = 1
        sufProd = 1
        maxProd = -inf
        for i in range(len(nums)) :
            preProd *= nums[i]
            sufProd *= nums[-(i+1)]
            maxProd = max(preProd, sufProd, maxProd)
            if preProd == 0 :
                preProd = 1
            if sufProd == 0 :
                sufProd = 1
        return maxProd