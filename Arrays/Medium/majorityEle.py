'''Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.'''

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = cnt = 0
         
        for i in nums :
            if cnt == 0:
                ele = i
            
            if i == ele:
                cnt+=1
            else:
                cnt-=1

        return ele