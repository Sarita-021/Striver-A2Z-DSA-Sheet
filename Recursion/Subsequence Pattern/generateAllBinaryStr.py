'''Given an integer N , Print all binary strings of size N which do not contain consecutive 1s.
A binary string is that string which contains only 0 and 1.

https://geeksforgeeks.org/problems/generate-all-binary-strings/1'''

def generateAllStrUtil(k, str, n, lst):
    if k == n:
        lst.append(''.join(str))
        return 
    
    if str[n-1] == '1':
        str[n] = '0'
        generateAllStrUtil(k, str, n+1, lst)
    
    if str[n-1] == '0':
        str[n] = '0'
        generateAllStrUtil(k, str, n+1, lst)
        str[n] = '1'
        generateAllStrUtil(k, str, n+1, lst)

class Solution:
    def generateBinaryStrings(self, k):
        # Code here
        lst = []
        str = ['0']*k
        
        generateAllStrUtil(k, str, 1, lst)
        
        str[0] = '1'
        generateAllStrUtil(k, str, 1, lst)
        
        return lst

