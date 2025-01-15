class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i,element in enumerate(nums):
            if i == 0 and element > target:
                return 0
            elif (element == target) or (element>target and nums[i-1]<target):
                return i
            elif i == len(nums) - 1:
                return i + 1
        