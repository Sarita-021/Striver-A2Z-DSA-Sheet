'''Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need 
to remove to make the rest of the intervals non-overlapping.
Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.
https://leetcode.com/problems/non-overlapping-intervals/description/'''

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals by end time
        intervals.sort(key=lambda x: x[1])
        
        cnt = 0  # Count of removed intervals
        prev_end = intervals[0][1]  # End time of last non-overlapping interval
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:  # Overlap detected
                cnt += 1
            else:
                prev_end = intervals[i][1]  # Update to new non-overlapping interval
        
        return cnt
