'''You are given the arrival times arr[] and departure times dep[] of all trains that arrive at a railway station on
the same day. Your task is to determine the minimum number of platforms required at the station to ensure that no train 
is kept waiting.
At any given time, the same platform cannot be used for both the arrival of one train and the departure of another.
Therefore, when two trains arrive at the same time, or when one arrives before another departs, additional platforms 
are required to accommodate both trains.
https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1'''

class Solution:    
    def minimumPlatform(self,arr,dep):
        arr.sort()
        dep.sort()

        ans = 1
        count = 1
        i = 1
        j = 0
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:  # one more platform needed
                count += 1
                i += 1
            else:  # one platform can be reduced
                count -= 1
                j += 1
            ans = max(ans, count)  # updating the value with the current maximum
        return ans
