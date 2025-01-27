'''Given an array of N integers and Q queries of indices. For each query indices[i], determine the count of elements 
in arr that are strictly greater than arr[indices[i]] to its right (after the position indices[i]).

https://www.geeksforgeeks.org/problems/number-of-nges-to-the-right/1/ '''


class Solution:
    def count_NGEs(self, N, a, indices):
        res = []
        for i in indices:
            count = 0
            idx = i+1
            while (idx < N):
                if (a[idx] > a[i]):
                    count += 1
                idx += 1
            res.append(count)
        return res