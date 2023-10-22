# Hayden Feddock

class Solution:
    def maxProfit(self, prices):

        minval = prices[0]
        profit = 0

        for i in range(1, len(prices)):

            # Replace the minimum value with the ith value if smaller
            minval = min(prices[i], minval)

            # Check the maximum profit value, and update if the new value is larger
            profit = max(prices[i] - minval, profit)
        
        return profit
