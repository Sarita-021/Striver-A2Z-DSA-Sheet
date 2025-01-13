'''Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using 
the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Input: ransomNote = "a", magazine = "b"
Output: false
'''

from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        rn_char_cnt = defaultdict(int)
        for c in ransomNote:
            rn_char_cnt[c] += 1

        mg_char_cnt = defaultdict(int)
        for c in magazine:
            mg_char_cnt[c] += 1
        
        for c in rn_char_cnt.keys():
            if c not in mg_char_cnt.keys():
                return False
            elif rn_char_cnt[c] > mg_char_cnt[c]:
                return False
        
        return True