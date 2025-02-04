'''Given a array arr of integers, return the sums of all subsets in the list.  Return the sums in any order.'''

class Solution:
    def subsetSums(self, arr):
        res = []

        def subsetsum(i, s):
            if len(arr) == i:
                res.append(s)
                return 
            
            subsetsum(i+1, s+arr[i])
            subsetsum(i+1, s)

        subsetsum(0, 0)
        return res