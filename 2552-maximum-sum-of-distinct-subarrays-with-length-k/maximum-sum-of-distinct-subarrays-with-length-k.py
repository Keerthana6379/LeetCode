class Solution(object):
    def maximumSubarraySum(self, nums, k):
        hs=set()
        n=len(nums)
        l=0
        sum,maxS=0,0

        for r in range(n):
            while nums[r] in hs:
                hs.remove(nums[l])
                sum-=nums[l]
                l+=1
            
            hs.add(nums[r])
            sum+=nums[r]

            if r-l+1==k:
                maxS=max(sum,maxS)
                hs.remove(nums[l])
                sum-=nums[l]
                l+=1
        return maxS
        