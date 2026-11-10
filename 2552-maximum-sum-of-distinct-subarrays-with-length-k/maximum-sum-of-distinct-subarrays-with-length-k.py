class Solution(object):
    def maximumSubarraySum(self, nums, k):
        hs=set()
        l=0
        sum=0
        mSum=0
        for r in range(len(nums)):
            while nums[r] in hs:
                hs.remove(nums[l])
                sum-=nums[l]
                l+=1
            
            hs.add(nums[r])
            sum+=nums[r]

            if r-l+1==k:
                mSum=max(sum,mSum)
                hs.remove(nums[l])
                sum-=nums[l]
                l+=1
            
        return mSum