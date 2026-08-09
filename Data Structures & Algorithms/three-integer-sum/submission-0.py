class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        
        for i in range(len(nums) - 1):
            seen = set()
            for j in range(i+1, len(nums)):
                need = -nums[i] - nums[j]
                if need in seen:
                    trio = tuple(sorted([nums[i], nums[j], need]))
                    result.add(trio)
                seen.add(nums[j])
                    

        return [list(trio) for trio in result]

