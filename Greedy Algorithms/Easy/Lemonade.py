'''At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in 
the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must
provide the correct change to each customer so that the net transaction is that the customer pays $5.
Note that you do not have any change in hand at first.
Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer 
with the correct change, or false otherwise.
https://leetcode.com/problems/lemonade-change/description/'''

from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if five:
                    five -= 1
                    ten += 1
                else :
                    return False
            else:
                if five and ten:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True