'''Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that have 
exactly k distinct characters. 
Input: S = "aba", K = 2
Output:3
Explanation:The substrings are: "ab", "ba" and "aba".'''

def atmost(s, k):
    l = 0
    cnt = 0
    freq = {}
    
    for r in range(len(s)):
        if s[r] in freq:
            freq[s[r]] += 1
        else:
            freq[s[r]] = 1
        
        while len(freq) > k:
            freq[s[l]] -= 1
            if freq[s[l]] == 0:
                del freq[s[l]]
            l += 1
        
        cnt += r - l + 1
    
    return cnt


class Solution:
    def substrCount (self,s, k):
        if len(s) == 0 :
            return 0
        elif k == 0 :
            return 0
        elif len(s) < k :
            return 0
        
        return atmost(s, k) - atmost(s, k-1)