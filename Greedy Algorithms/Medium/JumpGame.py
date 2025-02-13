'''You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array
represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
https://leetcode.com/problems/jump-game/'''

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxjump = 0
        n = len(nums)
        for i in range(n):
            if maxjump < i: return False
            maxjump = max(maxjump, i+nums[i])
            if maxjump >= n: return True
        return True