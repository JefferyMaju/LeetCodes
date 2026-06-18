class Solution(object):
    def removeElement(self, nums, val):
        for i in range(len(nums)):
            if nums[0] == val:
                nums.pop(0)
            else:
                nums.append(nums[0])
                nums.pop(0)
        return len(nums)
