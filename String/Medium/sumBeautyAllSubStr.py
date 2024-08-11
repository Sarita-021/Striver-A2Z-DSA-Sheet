'''The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.
For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.

Example 1:

Input: s = "aabcb"              Output: 5
Explanation: Substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.'''


class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s)) :
            dic = {}
            mf = 0
            for j in range(i, len(s)):
                if s[j] in dic:
                    dic[s[j]] += 1
                else :
                    dic[s[j]] = 1
                lf = min(dic.values())
                mf = max(mf, dic[s[j]])
                ans += mf - lf
                
        return ans
        