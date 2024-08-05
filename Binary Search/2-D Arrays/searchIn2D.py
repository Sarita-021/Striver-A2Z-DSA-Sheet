'''You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.'''

from typing import List

def findRow(arr, trg) :
    low = 0
    high = len(arr)-1
    while low <= high :
        mid = (low+high)//2
        if arr[mid][0] > trg :
            high = mid-1
        else :
            low = mid+1
    return high

def findCol(arr, trg) :
    low = 0
    high = len(arr)-1
    while low <= high :
        mid = (low+high)//2
        if arr[mid] > trg :
            high = mid-1
        elif arr[mid] < trg :
            low = mid+1
        else :
            return True
    return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = findRow(matrix, target)
        return findCol(matrix[col], target)