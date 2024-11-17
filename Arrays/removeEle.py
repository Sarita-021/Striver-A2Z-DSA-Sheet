''' Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.'''

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ne = 0
        for i, v in enumerate(nums):
            if v != val :
                nums[i], nums[ne] = nums[ne], nums[i]
                ne += 1
        return ne