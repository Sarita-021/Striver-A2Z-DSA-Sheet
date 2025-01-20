# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution(object):
    def rotate(self, nums, k):
        j=l=k%len(nums)
        s = len(nums)
        for i in range(0,len(nums)/2):
            nums[i],nums[-(i+1)] = nums[-(i+1)],nums[i]
        for i in range(0,j/2):
            j-=1
            nums[i],nums[j] = nums[j], nums[i]
        for i in range(l,(s+l)/2):
            s-=1
            nums[i], nums[s] = nums[s], nums[i]
        return nums