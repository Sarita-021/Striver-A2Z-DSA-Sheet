'''Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.'''

from math import floor
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cntDic = {}
        for i in nums :
            if i in list(cntDic.keys()):
                cntDic[i] += 1
            else :
                cntDic[i] = 1
        
        res = []
        minLim = floor(len(nums)/3)

        for i in list(cntDic.keys()) :
            if cntDic[i] > minLim :
                res.append(i)
        
        return res