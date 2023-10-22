# Hayden Feddock

class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        # Recusive top-down function to calculate the max profit with the conditions
        def calcProfit(self, nums, i):

            # If the index is greater than the length then return 0
            if i >= len(nums):
                return 0

            # If the index is already in the cache then use that
            elif i in memo:
                return memo[i]

            # Calculate the profit by recursively calling the function with the next and second values
            else:
                profit = max(calcProfit(self, nums, i+1), nums[i] + calcProfit(self, nums, i+2))
                memo[i] = profit
                return profit

        # Return the profit with the recursive function
        return calcProfit(self, nums, 0)
            