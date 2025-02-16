'''The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).

Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 
or more times) with the concatenation of the character and the number marking the count of the characters (length of the run).
For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and 
replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.
https://leetcode.com/problems/count-and-say/'''

# Optimized solution

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        ans = "1"
        for _ in range(n - 1):
            new_ans = []
            count = 1
            for j in range(1, len(ans)):
                if ans[j] == ans[j - 1]:
                    count += 1
                else:
                    new_ans.append(str(count) + ans[j - 1])
                    count = 1
            new_ans.append(str(count) + ans[-1])  # Append last counted group
            ans = "".join(new_ans)  # Efficient string construction
        
        return ans
    
# Solution using Helper function

def mapDigitFreq(s):
    maplst = list()
    for i in range(len(s)):
        if i != 0 and s[i] == s[i-1]:
            maplst[-1][0] += 1
        else :
            maplst.append([1,s[i]])
    return maplst

def createStr(lst):
    s = ''
    for ele in lst:
        s = s + str(ele[0]) + ele[1]
    return s

class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        i = 1
        while i < n:
            ans = mapDigitFreq(ans)
            ans = createStr(ans)
            i += 1
        return ans