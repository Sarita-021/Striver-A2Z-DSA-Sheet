'''There are several cards arranged in a row, and each card has an associated number of points. The points are given in 
the integer array cardPoints. In one step, you can take one card from the beginning or from the end of the row. You have 
to take exactly k cards. Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/'''

from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_sum = sum(cardPoints)  # Get total sum of the array
        # Initial sum of the first k elements (this is the "left sum")
        current_sum = sum(cardPoints[:k])
        maxsum = current_sum  # Initialize maxsum as current_sum
        
        # Start sliding the window
        for i in range(k):
            # Slide the window by removing one element from the left and adding one from the right
            current_sum -= cardPoints[k - i - 1]
            current_sum += cardPoints[-i - 1]
            maxsum = max(maxsum, current_sum)  # Keep track of the maximum score
            
        return maxsum
