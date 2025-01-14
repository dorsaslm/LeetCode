class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        previous=nums[0]
        underlines=0
        i = 1
    
        while i < len(nums):
            if nums[i] == previous:
                nums.pop(i)
            else:
                previous = nums[i]
                i += 1
        
        return len(nums)



        