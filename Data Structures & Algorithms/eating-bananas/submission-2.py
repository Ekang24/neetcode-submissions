class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speedy = max(piles)
        slowy = 1
        
        while slowy <= speedy:
            time = 0
            midy = (slowy + speedy) // 2
            for pile in piles:
                time += math.ceil(pile / midy)
            if time > h:
                slowy = midy + 1
            else:
                speedy = midy - 1
        return slowy

        