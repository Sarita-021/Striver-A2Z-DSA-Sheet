'''You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and 
the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval 
= [start, end] that represents the start and end of another interval. Insert newInterval into intervals such that intervals is
still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping 
intervals if necessary).

Return intervals after the insertion.
Note that you don't need to modify intervals in-place. You can make a new array and return it.
https://leetcode.com/problems/insert-interval/description/'''

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        if i != n:
            newInterval[0] = min(intervals[i][0], newInterval[0])
        
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        
        ans.append(newInterval)

        while i < n:
            ans.append(intervals[i])
            i += 1
        
        return ans