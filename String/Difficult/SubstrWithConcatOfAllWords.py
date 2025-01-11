'''You are given a string s and an array of strings words. All the strings of words are of the same length.
A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.
For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all 
concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

https://leetcode.com/problems/substring-with-concatenation-of-all-words/ '''


from collections import defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        
        substr_len = len(words) * len(words[0])
        word_len = len(words[0])
        result = []
        
        for i in range(len(s) - substr_len + 1):
            seen = defaultdict(int)
            for j in range(i, i + substr_len, word_len):
                word = s[j:j+word_len]
                if word in word_count:
                    seen[word] += 1
                    if seen[word] > word_count[word]:
                        break
                else:
                    break
            else:
                result.append(i)
        
        return result
    
'''How the else Clause Works with Loops
The else block attached to a for or while loop executes only if the loop completes without a break statement being encountered.'''