'''Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array,
which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

https://leetcode.com/problems/next-greater-element-ii/description/ '''

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        s = [nums[-1]]
        res = [0] * len(nums) 
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < s[-1]:
                s.append(nums[i])
            else:
                while s and nums[i] >= s[-1]:
                    s.pop()
                s.append(nums[i])

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < s[-1] :
                res[i] = s[-1]
            else:
                while s and nums[i] >= s[-1]:
                    s.pop()
                if not s:
                    res[i] = -1
                else :
                    res[i] = s[-1]
            s.append(nums[i])

        return res