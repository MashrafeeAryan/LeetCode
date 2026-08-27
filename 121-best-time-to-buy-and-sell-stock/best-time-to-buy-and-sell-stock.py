class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            We need to keep track of the best_profit so far and lowest buy day
            Brute force would be just use two loops
            however, we can optimize it and use one loop
            1. best_profit = 0
            2. lowest_buy_day = price[0]
            3. for current_day in prices:
                4. profit = current day - lowest buy day.
                5. we find if it is our best profit so far using max(best_profit, profit)
                6. We then also check if we encounter lowest_buy day a nother one lower than this one
        """

        best_profit = 0
        lowest_buy = prices[0]
        for current_day in prices:
            profit = current_day - lowest_buy
            best_profit = max(best_profit, profit)

            lowest_buy = min(lowest_buy, current_day)

        return best_profit