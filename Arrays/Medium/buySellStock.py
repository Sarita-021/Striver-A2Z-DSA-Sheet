'''You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        bday = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < bday:
                bday = prices[i]
                continue
            profit = prices[i] - bday
            if maxProfit < profit:
                maxProfit = profit
        
        return maxProfit