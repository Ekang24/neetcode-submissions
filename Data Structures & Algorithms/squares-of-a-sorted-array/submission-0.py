class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[right] ** 2 < nums[left] ** 2:
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
        return res
        