class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                cur_profit = prices[i] - min_price
                if cur_profit > max_profit:
                    max_profit = cur_profit
        return max_profit
