'''Given a pair of strings of equal lengths, Geek wants to find the better string. The better string is the string having
more number of distinct subsequences.
If both the strings have equal count of distinct subsequence then return str1.
https://www.geeksforgeeks.org/problems/better-string/1'''


# Recursive solution and by using DP 
def count_subseq(s):
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        last = [-1] * 26

        for i in range(1, n + 1):
            dp[i] = 2 * dp[i - 1]
            if last[ord(s[i - 1]) - 97] != -1:
                dp[i] = dp[i] - dp[last[ord(s[i - 1]) - 97]]

            last[ord(s[i - 1]) - 97] = i - 1
        return dp[n]

class Solution:
    def betterString(self, str1, str2):
        a = count_subseq(str1)
        b = count_subseq(str2)

        if a >= b:
            return str1
        else:
            return str2