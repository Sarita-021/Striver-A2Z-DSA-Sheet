'''A permutation of an array of integers is an arrangement of its members into a sequence or linear order.'''

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n1 = -1
        for i in range(len(nums)-2, -1,-1) :
            if nums[i] < nums[i+1] :
                n1 = i
                break
        
        if n1 == -1 :
            nums.reverse()
        else :
            for i in range(len(nums)-1, n1, -1) :
                if nums[n1] < nums[i] :
                    nums[n1], nums[i] = nums[i], nums[n1]
                    break
            
            nums[:] = nums[:n1+1] + nums[n1+1:][::-1]