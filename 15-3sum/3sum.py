class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        firstSum = 0
        length = len(nums)
        seen = set()
        output = []
        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = length -1
            while left < right:
                sum = nums[i]+nums[left]+nums[right]
                if sum == 0:
                    output.append([nums[i],nums[left],nums[right]])
                    left = left + 1
                    right = right -1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while right > left and nums[right] == nums[right+1]:
                        right-=1
                elif sum > 0:
                    right -=1
                elif sum < 0:
                    left += 1
        return output


            
       
       