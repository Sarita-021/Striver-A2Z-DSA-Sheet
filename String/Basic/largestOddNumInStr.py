'''You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) 
that is a non-empty substring of num, or an empty string "" if no odd integer exists.
A substring is a contiguous sequence of characters within a string.'''


class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if num[i] in ['1','3','5','7','9'] :
                return num[:i+1]
        return ""