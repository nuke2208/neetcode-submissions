class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        n = len(prices)
        max_profit = 0
        while right < n:
            profit = prices[right] - prices[left]
            if prices[right] < prices[left]:
                left = right
            if profit > max_profit:
                max_profit = profit
            right = right + 1
            
        return max_profit
        