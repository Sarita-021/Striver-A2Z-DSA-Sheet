'''Given an array of integers citations where citations[i] is the number of citations a researcher 
received for their ith paper, return the researcher's h-index.
According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that 
the given researcher has published at least h papers that have each been cited at least h times.

'''

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        i = 0
        while i < len(citations) and i+1 <= citations[i]:
            i += 1
        return i
    
    

'''Formally, if f is the function that corresponds to the number of citations for each publication, we compute the
h-index as follows: First we order the values of f from the largest to the lowest value. Then, we look for the last
position in which f is greater than or equal to the position (we call h this position). For example, if we have a 
researcher with 5 publications A, B, C, D, and E with 10, 8, 5, 4, and 3 citations, respectively, the h-index is 
equal to 4 because the 4th publication has 4 citations and the 5th has only 3. In contrast, if the same 
publications have 25, 8, 5, 3, and 3 citations, then the index is 3 (i.e. the 3rd position) because the fourth 
paper has only 3 citations.

f(A)=10, f(B)=8, f(C)=5, f(D)=4, f(E)=3　→ h-index=4
f(A)=25, f(B)=8, f(C)=5, f(D)=3, f(E)=3　→ h-index=3'''