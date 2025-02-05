'''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/'''


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index, path):
            if index == len(digits):  # Base case: Full combination formed
                res.append("".join(path))
                return
            for char in digit_map[digits[index]]:
                path.append(char)     # Choose
                backtrack(index + 1, path)  # Explore next digit
                path.pop()            # Undo choice (Backtrack)
        
        backtrack(0, [])
        return res