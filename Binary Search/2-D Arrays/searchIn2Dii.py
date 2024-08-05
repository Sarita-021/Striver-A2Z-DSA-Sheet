'''Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.'''

from typing import List


def searchElement(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    row = 0
    col = m - 1

    while row < n and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return searchElement(matrix, target)
        