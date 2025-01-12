'''You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
 DO NOT allocate another 2D matrix and do the rotation.'''

import math
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(math.floor(len(matrix)/2)) :
            for j in range(math.ceil(len(matrix)/2)) :
                bi1 = -(i+1)
                bi2 = -(j+1)
                matrix[j][bi1], matrix[bi1][bi2], matrix[bi2][i], matrix[i][j] = matrix[i][j], matrix[j][bi1], matrix[bi1][bi2], matrix[bi2][i]
