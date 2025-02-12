'''Given two arrays, val[] and wt[], representing the values and weights of items, and an integer capacity representing the 
maximum weight a knapsack can hold, determine the maximum total value that can be achieved by putting items in the knapsack.
You are allowed to break items into fractions if necessary.
Return the maximum value as a double, rounded to 6 decimal places.
https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1'''

class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, val, wt, capacity):
        ratio = [(v / w, v, w) for v, w in zip(val, wt)]
        
        # Sort by ratio in descending order
        ratio.sort(reverse=True, key=lambda x: x[0])  
        
        # Extract sorted values and weights
        val = [x[1] for x in ratio]
        wt = [x[2] for x in ratio]
        
        # Another way to sort 2 arrays simultaneously
        # sorted_items = sorted(zip(values, weights), key=lambda x: x[0] / x[1], reverse=True)
        # sorted_values, sorted_weights = zip(*sorted_items)

        
        l = r = 0
        maxval = 0
        while r < len(wt) and capacity>0:
            if capacity >= wt[r]:
                maxval += val[r]
            else:
                maxval += (val[r]/wt[r])*capacity
            capacity -= wt[r]
            r += 1
            
