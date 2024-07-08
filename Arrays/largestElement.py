from typing import List
class Solution:
    def largest(self, n : int, arr : List[int]) -> int:
        lrg = arr[0]
        for i in range(1,n):
            if (arr[i] > lrg):
                lrg = arr[i]
        return lrg