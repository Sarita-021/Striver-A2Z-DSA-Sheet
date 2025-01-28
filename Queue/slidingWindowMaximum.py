'''You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array
to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

https://leetcode.com/problems/sliding-window-maximum/description/ '''

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        deque = []
        for i in range(len(nums)):
            if deque and deque[0] == i-k:
                deque.pop(0)
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
            if i >= k-1:
                ans.append(nums[deque[0]])
        return ans