'''We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array 
represent their relative position in space. For each asteroid, the absolute value represents its size, and the sign 
represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

https://leetcode.com/problems/asteroid-collision/description/ '''

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                # If the current asteroid is smaller (absolute value), destroy it
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                # If the current asteroid is equal in size, destroy both
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                # No collision, add the asteroid to the stack
                stack.append(asteroid)
        return stack