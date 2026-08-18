class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        good = 0
        for num in nums:
            if num in seen:
                good += seen[num]
            seen[num] = seen.get(num, 0 ) + 1
        return good