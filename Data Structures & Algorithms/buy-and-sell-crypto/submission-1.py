class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        left = 0
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                profit = prices[right] - prices[left]
                if profit > maxi:
                    maxi = profit
                else:
                    continue
        return maxi



        