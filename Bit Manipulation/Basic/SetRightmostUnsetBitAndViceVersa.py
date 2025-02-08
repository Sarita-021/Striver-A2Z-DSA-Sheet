'''Given a non-negative number n . The problem is to set the rightmost unset bit in the binary representation of n.
https://www.geeksforgeeks.org/problems/set-the-rightmost-unset-bit4436/1'''

class Solution:
	def setBit(self, n):
		# code here
		return n | (n + 1)

'''Given a non-negative number n . The problem is to unset the rightmost set bit in the binary representation of n.'''

class Solution:
	def setBit(self, n):
		# code here
		return n & (n - 1)