class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = []
        good = 0
        for num in nums:
            if num in seen:
                good += seen.count(num)
            seen.append(num)
        return good