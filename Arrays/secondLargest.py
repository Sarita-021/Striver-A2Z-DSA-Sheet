class Solution:
    def print2largest(self, arr):
        lrg = arr[0]
        lrg2 = -1
        for i in range(1, len(arr)):
            if (arr[i] > lrg):
                lrg2 = lrg
                lrg = arr[i]
            elif (arr[i] > lrg2 and arr[i] != lrg):
                lrg2 = arr[i]
        return lrg2