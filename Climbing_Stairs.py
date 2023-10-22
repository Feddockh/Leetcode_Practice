# Hayden Feddock

class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def distinctCount(self, n: int) -> int:

            # Check if the base case has been reached
            if n < 0:
                return 0
            elif n == 0 or n == 1:
                return 1
            else:

                # Check if the value is already in memory
                if (n in memo):

                    # Return the value we already have
                    return memo[n]

                else:
                    # Get the count of the remaining combinations if 1 step or 2 steps are taken and add the sum
                    count = distinctCount(self, n - 1) + distinctCount(self, n - 2)

                    # Update the memory
                    memo[n] = count

                    # Return the new count
                    return count

        return distinctCount(self, n)