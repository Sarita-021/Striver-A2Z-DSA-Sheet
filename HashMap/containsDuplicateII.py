'''Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the
array such that nums[i] == nums[j] and abs(i - j) <= k.

Input: nums = [1,2,3,1], k = 3
Output: true'''

from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        distinct = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in distinct.keys():
                if abs(distinct[nums[i]] - i) <= k:
                    return True
                else:
                    distinct[nums[i]] = i
            distinct[nums[i]] = i
        return False