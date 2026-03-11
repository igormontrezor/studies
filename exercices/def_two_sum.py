class Solution:
    def twoSum(self, nums, target):
        for c in range(len(nums)):
            for b in range(c+1, len(nums)):
                if (nums[c] + nums[b] == target):
                    return [c, b]
                
param_1 = [2,5,5,11]
param_2 = 10    
ret = Solution().twoSum(param_1, param_2)

class Solution:
    def twoSum(self, nums, target):
        c = 0
        while c < len(nums):
            for b in range(c+1, len(nums)):
                if (nums[c] + nums[b] == target):
                    return [c, b]
            c += 1   
param_1 = [2,5,5,11]
param_2 = 10    
ret = Solution().twoSum(param_1, param_2)
print(ret)