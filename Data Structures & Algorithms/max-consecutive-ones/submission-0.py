class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        cons = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                
                left = right + 1
            else:
                cons = max(cons, right - left + 1)
            
        return cons
            
        