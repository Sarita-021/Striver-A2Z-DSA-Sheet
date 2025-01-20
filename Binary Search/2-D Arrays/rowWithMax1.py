'''You are given a 2D array consisting of only 1's and 0's, where each row is sorted in non-decreasing order.
You need to find and return the index of the first row that has the most number of 1s. If no such row exists, return -1.'''

def cntOne(arr) :
    low = 0
    high = len(arr)-1
    while low <= high :
        mid = (low+high)//2
        if arr[mid] == 1 :
            high = mid-1
        else :
            low = mid+1
    return len(arr)-low
    
class Solution:
    def rowWithMax1s(self, arr):
        currMax = 0
        ans = -1
        for i in range(len(arr)):
            cnt = cntOne(arr[i])
            if currMax < cnt :
                ans = i
                currMax = cnt
        return ans