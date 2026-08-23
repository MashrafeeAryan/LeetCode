class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = prices[0]
        best_profit = 0

        for current_price in prices:
            if current_price < best_buy:
                best_buy = current_price
            else:
                profit = current_price - best_buy
                best_profit = max(best_profit, profit)
        
        return best_profit