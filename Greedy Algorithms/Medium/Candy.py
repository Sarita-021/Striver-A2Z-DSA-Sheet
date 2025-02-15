'''There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

https://leetcode.com/problems/candy/description/'''

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        totalCandies = 1
        i = 1
        n = len(ratings)
        while i < n:
            if (ratings[i] == ratings[i-1]):
                totalCandies += 1
                i += 1
                continue
        
            peak = 1
            while (i < n and ratings[i] > ratings[i-1]):
                peak += 1
                totalCandies += peak
                i += 1
            
            down = 1
            while (i < n and ratings[i] < ratings[i-1]):
                totalCandies += down
                down += 1
                i += 1
            
            if down > peak:
                totalCandies += down - peak
            
        return totalCandies