class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # greedy solution
        # at each step make the best choice, dont revisit
        # always buy lowest price seen
        # check if selling today is best result in best profit
        profit = 0
        buy = prices[0]


        for price in prices:
            profit = max(profit, price - buy)

            if price < buy:
                buy = price

        return profit