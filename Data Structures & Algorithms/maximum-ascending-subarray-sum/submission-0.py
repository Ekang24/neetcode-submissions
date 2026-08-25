class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        current = nums[0]
        total = nums[0]
        for i in range(1, len(nums)):
        
            if nums[i] > nums[i-1]:
                current += nums[i]
            else:
                current = nums[i]
            total = max(total, current)
            
            
        return total
            
            
            

            


        