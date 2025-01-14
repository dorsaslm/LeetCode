class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        previous=nums[0]
        underlines=0
        i = 1
        k = 1

        for i in range (1,len(nums)):
            if nums[i] != nums[k - 1]:  # Compare with the last unique element
                nums[k] = nums[i]  # Place the unique element at the `k` index
                k += 1
    
        #while i < len(nums):
        #    if nums[i] == previous:
        #        nums.pop(i)
        #    else:
        #        previous = nums[i]
        #        i += 1
        
        return k



        