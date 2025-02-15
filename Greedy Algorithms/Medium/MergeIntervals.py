'''Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array
of the non-overlapping intervals that cover all the intervals in the input.
https://leetcode.com/problems/merge-intervals/description/'''

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda  x:x[0])
        merged=[]
        for interval in (intervals):
            if not merged or merged[-1][1]<interval[0]:
                merged.append(interval)
            else:
                merged[-1][1]=max(merged[-1][1], interval[1])
        return merged 