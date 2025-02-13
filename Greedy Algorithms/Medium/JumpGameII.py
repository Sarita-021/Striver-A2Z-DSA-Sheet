'''You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], 
you can jump to any nums[i + j] where
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
https://leetcode.com/problems/jump-game-ii/'''

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = l = r = 0
        n = len(nums)
        while r < n-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(i+nums[i], farthest)
            l = r+1
            r = farthest
            jump += 1

        return jump