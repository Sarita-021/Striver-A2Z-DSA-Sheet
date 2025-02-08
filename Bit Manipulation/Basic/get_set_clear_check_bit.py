'''Given a 32 bit unsigned integer num and an integer i. Perform following operations on the number - 
1. Get ith bit
2. Set ith bit
3. Clear ith bit
0- based indexing is considered for bits, indexing starts from the rightmost bit as 0.
https://www.geeksforgeeks.org/problems/bit-manipulation-1666686020/1'''

class Solution:
    def bitManipulation(self, num, i):
        def get_ith_bit(num, i):
            return (num & (1 << i)) >> i
        
        def set_ith_bit(num, i):
            return num | (1 << i)
        
        def clear_ith_bit(num, i):
            return num & ~(1 << i)
        
        def checkKthBit(num, i):
            return True if (num & (1 << i)) >> i == 1 else False

        ithBit = get_ith_bit(num, i)
        setithBit = set_ith_bit(num, i)
        clearithBit = clear_ith_bit(num, i)
        print(f'{ithBit} {setithBit} {clearithBit} {checkKthBit(num, i)}')