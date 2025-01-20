'''Given a string s and an integer k, return true if you can use all the characters in s to construct 
k palindrome strings or false otherwise.
Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Hint 1
If the s.length < k we cannot construct k strings from s and answer is false.
Hint 2
If the number of characters that have odd counts is > k then the minimum number of palindrome
strings we can construct is > k and answer is false.
Hint 3
Otherwise you can construct exactly k palindrome strings and answer is true.
'''

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        chrcnt = {}
        for i in s:
            if i in chrcnt.keys():
                chrcnt[i] += 1
            else :
                chrcnt[i] = 1
        
        cnt = 0
        for v in chrcnt.values():
            if v%2 == 1:
                cnt += 1
        
        if cnt > k:
            return False
        
        return True