class Solution(object):
    def longestConsecutive(self, nums):
        dis=set(nums)
        longest=0
        for val in dis:
            if (val-1) not in dis:
                length=1
                while (val+length) in dis:
                    length+=1
                longest=max(longest,length)
        return longest
        