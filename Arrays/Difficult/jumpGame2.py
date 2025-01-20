'''You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you
 are at nums[i], you can jump to any nums[i + j] where:
-> 0 <= j <= nums[i] and
-> i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can 
reach nums[n - 1].'''

### Solution 1 :     Using extra space

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        j = [float('inf')]*n     #for storing min jumps req for reaching index i
        j[0] = 0
        i = 0
        while i < n or j[-1] == 'Inf':
            l = i
            while l < i+nums[i-1] and l < n:
                j[l] = min(j[i-1]+1,j[l])
                l += 1
            i+=1

        return j[-1]
    

### Solution 2:    Without extra space

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res , l , r = 0 , 0 , 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range( l , r + 1 ):
                n = i + nums[i]
                farthest = farthest if farthest > n else n
            l = r + 1
            r = farthest
            res += 1
        return res