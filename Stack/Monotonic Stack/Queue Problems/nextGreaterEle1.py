'''The next greater element of some element x in an array is the first greater element that is to the right of x 
in the same array.You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next
greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

https://leetcode.com/problems/next-greater-element-i/description/ '''

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = [nums2[-1]]
        res = {nums2[-1]:-1}
        
        for i in range(len(nums2)-2, -1, -1):
            if nums2[i] < s[-1] :
                res[nums2[i]] = s[-1]
            else:
                while s and nums2[i] > s[-1]:
                    s.pop()
                if not s:
                    res[nums2[i]] = -1
                else :
                    res[nums2[i]] = s[-1]
            s.append(nums2[i])
            
        ans = []
        for i in nums1:
            ans.append(res[i])

        return ans