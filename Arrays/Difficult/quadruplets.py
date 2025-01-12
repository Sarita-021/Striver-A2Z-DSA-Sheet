'''Given an array nums of n integers, return an array of all the unique 
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n ; a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.'''

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-3) :
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2) :
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                req = target - (nums[i] + nums[j])
                k = j+1
                l = len(nums)-1
                while k<l:
                    curr = nums[k] + nums[l]
                    if req == curr :
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                        k += 1
                        while nums[k] == nums[k-1] and k<l :
                            k+=1

                        l -= 1
                        while nums[l] == nums[l+1] and k<l :
                            l-=1
                    elif curr < req :
                        k += 1
                    else :
                        l -= 1
        
        return res

            
        