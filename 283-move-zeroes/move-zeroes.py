class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        l=0
        for r in range(n):
            if nums[r]!=0:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
        