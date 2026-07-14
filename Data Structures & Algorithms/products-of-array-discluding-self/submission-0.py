class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i=0
        new=[1]*len(nums)
        while i < len(nums):
            p=1
            for j in range(len(nums)):
                if j==i:
                    p*=1
                else:
                    p*=nums[j]
            new[i]=p
            i+=1
        return new

