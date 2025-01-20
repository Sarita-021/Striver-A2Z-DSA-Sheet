'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I               '''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        row = 0
        if numRows == 1 or numRows >= len(s): return s
        while row < numRows :
            ptr = 0
            d = 0
            for i in range(len(s)):
                if ptr == row:
                    ans += s[i]

                if ptr == 0:
                    d = 1
                elif ptr == numRows-1:
                    d = -1
                ptr += d

            row += 1
        return ans