'''Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.'''


class Solution:
    def frequencySort(self, s: str) -> str:
        count = defaultdict(int) 
        for c in s: count[c] += 1
        return "".join([a[1] * a[0] for a in sorted([[count[c], c] for c in count], reverse=True)])
    

# OR Explained code of above solution

from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        count = defaultdict(int)
        for c in s:
            count[c] += 1

        # Step 2: Create a list of [frequency, character] pairs
        freq_list = []
        for c in count:
            freq_list.append([count[c], c])

        # Step 3: Sort the list of pairs by frequency in descending order
        sorted_freq_list = sorted(freq_list, reverse=True)

        # Step 4: Build the result string by repeating characters according to their frequency
        result = []
        for a in sorted_freq_list:
            print(a)  # Print the current pair [frequency, character]
            result.append(a[1] * a[0])

        # Step 5: Join the result list into a final string and return it
        return "".join(result)
