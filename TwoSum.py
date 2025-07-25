class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i):
                if i!=j and nums[i]+nums[j]==target:
                    return [j,i]
        
