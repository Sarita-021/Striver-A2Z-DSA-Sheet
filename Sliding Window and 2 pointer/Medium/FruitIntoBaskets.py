'''Given an array arr[] containing positive elements, the task is to find the length of the longest subarray of an input 
array containing at most two distinct integers.
https://www.geeksforgeeks.org/problems/fruit-into-baskets-1663137462/1'''

from collections import defaultdict

class Solution:
    def totalElements(self, arr):
        l = 0
        unqele = defaultdict(int)
        
        for r in range(len(arr)):
            unqele[arr[r]] += 1

            if len(unqele) > 2:  # Reduce the window size if unique elements exceed 2
                unqele[arr[l]] -= 1
                if unqele[arr[l]] == 0:
                    del unqele[arr[l]]
                l += 1  # Move left pointer
        
        return r - l + 1  # The longest valid subarray size
