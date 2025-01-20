class Solution(object):
    def removeDuplicates(self, nums):
        cnt = 1
        j = 0
        for i in range(1, len(nums)):
            if (nums[j] == nums[i]) :
                continue
            cnt += 1
            j += 1
            nums[j], nums[i] = nums[i], nums[j]
        return cnt