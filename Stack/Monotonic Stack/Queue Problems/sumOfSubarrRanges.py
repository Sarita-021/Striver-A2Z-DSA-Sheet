'''You are given an integer array nums. The range of a subarray of nums is the difference between the largest and 
smallest element in the subarray. Return the sum of all subarray ranges of nums.
A subarray is a contiguous non-empty sequence of elements within an array.
https://leetcode.com/problems/sum-of-subarray-ranges/description/ '''

from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        inf = float('inf')
        A = [-inf] + nums + [-inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res -= A[j] * (i - j) * (j - k)
            s.append(i)
            
        A = [inf] + nums + [inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] < x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res