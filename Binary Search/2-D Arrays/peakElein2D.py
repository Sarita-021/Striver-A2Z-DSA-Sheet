'''A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors
to the left, right, top, and bottom. Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, 
find any peak element mat[i][j] and return the length 2 array [i,j].
You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.'''


from typing import List

def maxEle(mat):
    m = -1
    ans = -1
    for i in range(len(mat)):
        if m < mat[i] :
            m = mat[i]
            ans = i
    return ans

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        low, high = 0, len(mat)-1
        l = len(mat)
        while (low<=high):
            mid = (low+high)//2
            mEle = maxEle(mat[mid])
            if mid-1 >= 0 and mat[mid][mEle] < mat[mid-1][mEle]:
                high = mid-1
            elif mid+1 < l and mat[mid][mEle] < mat[mid+1][mEle]:
                low = mid + 1
            else :
                return [mid,mEle]
        return -1