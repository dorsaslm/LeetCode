class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}
        for i,num in enumerate(nums):
            compliment = target - num
            if compliment in nummap:
                return[i,nummap[compliment]]
            nummap[num] = i
            
'''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if  nums[i]+nums[j] == target:
                    return [i,j]
                else:
                    continue '''

             
        