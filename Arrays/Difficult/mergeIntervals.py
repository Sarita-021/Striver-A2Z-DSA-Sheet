'''Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and 
return an array of the non-overlapping intervals that cover all the intervals in the input.'''


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = [[]]
        n = len(intervals)
        intervals.sort()
        ans[0] = intervals[0]
        cnt = 0
        for i in range(n):
            if (intervals[i][0] > ans[cnt][1]) :
                ans.append(intervals[i])
                cnt += 1
            elif (intervals[i][1] > ans[cnt][1]):
                ans[cnt][1] = intervals[i][1]
        return ans