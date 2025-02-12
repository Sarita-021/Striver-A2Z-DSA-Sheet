'''Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/'''

#shorter and more intuitive solution

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ls = [-1, -1, -1]  
        count = 0  
        for i in range(len(s)):  
            ls[ord(s[i]) - ord('a')] = i  
            if -1 not in ls:  
                count += 1 + min(ls)  
        return count
    
# Sliding window solution

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = { 'a': 0, 'b': 0, 'c': 0 }
        left = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] += 1  # Expand window by including s[right]

            while all(count.values()):  # If all characters are present
                count[s[left]] -= 1  # Shrink window from the left
                left += 1
            
            result += left  # Count valid substrings

        return result
