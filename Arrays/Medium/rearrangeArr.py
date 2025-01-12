'''You should return the array of nums such that the the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.'''


import math
from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in nums :
            if i >= 0 :
                pos.append(i)
            else :
                neg.append(i)
        
        for i in range(math.floor(len(nums)/2)) :
            nums[i*2] = pos[i]
            nums[i*2+1] = neg[i]

        return nums