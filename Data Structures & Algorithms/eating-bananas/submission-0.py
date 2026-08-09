class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini = 1
        maxi = max(piles)
        k = maxi
        
        while mini <= maxi:
            hrs = 0
            mid = (mini + maxi) // 2
            for num in piles:
                hrs += math.ceil(num / mid)
            if hrs <= h:
                k = mid
                maxi = mid - 1
                


            else:
                mini = mid + 1
        return k
            



            



            

            



        