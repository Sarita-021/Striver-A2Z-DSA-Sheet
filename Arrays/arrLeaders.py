'''Given an array arr of n positive integers, your task is to find all the leaders in the array. 
An element of the array is considered a leader if it is greater than all the elements on its right side or if 
it is equal to the maximum element on its right side. The rightmost element is always a leader.'''

class Solution:
    #Back-end complete function Template for Python 3   
    
    #Function to find the leaders in the array.
    def leaders(self,n, arr):
        #Code here
        l = [arr[-1]]
        currl = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            if arr[i]>=currl:
                l.insert(0,arr[i])
                currl = arr[i]
        return l 