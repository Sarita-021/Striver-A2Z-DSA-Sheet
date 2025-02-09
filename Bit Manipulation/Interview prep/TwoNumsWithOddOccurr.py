'''Given an unsorted array, Arr[] of size N and that contains even number of occurrences for all numbers except two numbers. 
Find the two numbers in decreasing order which has odd occurrences.
https://www.geeksforgeeks.org/problems/two-numbers-with-odd-occurrences5846/1'''


class Solution:
    def twoOddNum(self, Arr, N):
        x = 0
        for i in Arr:
            x = x^i
        
        rightMost = (x&(x-1))^x
        b1 = 0
        b2 = 0
        for i in Arr:
            if i&rightMost:
                b1 = b1^i
            else :
                b2 = b2^i
        
        return [b1, b2] if b1 > b2 else [b2, b1]