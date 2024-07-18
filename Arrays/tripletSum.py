'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such 
that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.'''

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for x in range(len(nums)-2) :
            if x > 0 and nums[x] == nums[x-1]:
                continue
            y = x+1
            z = len(nums) -1
            while y<z :
                s = nums[x] + nums[y] + nums[z]
                if s == 0 :
                    res.append([nums[x],nums[y],nums[z]])
                    y += 1
                    while nums[y] == nums[y-1] and y<z :
                        y+=1

                    z -= 1
                    while nums[z] == nums[z+1] and y<z :
                        z-=1
                        
                elif s < 0:
                    y += 1
                else :
                    z -= 1
        
        return res