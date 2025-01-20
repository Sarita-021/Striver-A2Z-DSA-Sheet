'''Given a sorted array arr[] of size n without duplicates, and given a value x. Floor of x is defined as the 
largest element k in arr[] such that k is smaller than or equal to x. Find the index of k(0-based indexing).'''


class Solution:
    def findFloor(self,A,N,X):
        low = 0
        high = N-1
        while low<=high:
            mid = (low+high)//2
            if X < A[mid] :
                high = mid-1
            else : 
                low = mid+1
        return high