'''You are given timings of n meetings in the form of (start[i], end[i]) where start[i] is the start time of meeting i and 
end[i] is the finish time of meeting i. Return the maximum number of meetings that can be accommodated in a single meeting 
room, when only one meeting can be held in the meeting room at a particular time. 
https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1'''

class Meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos

class Solution:
    def maximumMeetings(self,start,end):
        meet = [Meeting(start[i], end[i], i+1) for i in range(len(start))]
        meet = sorted(meet, key = lambda x: (x.end, x.pos))
        cnt = 1
        limit = meet[0].end
        for i in range(1, len(start)):
            if meet[i].start > limit:
                limit = meet[i].end
                cnt += 1
        return cnt