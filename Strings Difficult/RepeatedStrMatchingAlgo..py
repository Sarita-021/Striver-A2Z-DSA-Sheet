'''Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of 
it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.
Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".
https://leetcode.com/problems/repeated-string-match/description/ '''

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeat_count = 1
        repeated_a = a
        
        # Keep repeating 'a' until its length is at least 'b'
        while len(repeated_a) < len(b):
            repeated_a += a
            repeat_count += 1
        
        # Check if 'b' is a substring of the current repeated 'a'
        if b in repeated_a:
            return repeat_count
        
        # One more repetition to check cross-boundary cases
        repeated_a += a
        repeat_count += 1
        
        if b in repeated_a:
            return repeat_count
        
        # If 'b' is still not found, it's impossible
        return -1