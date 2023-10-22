# I did struggle with this one because I was unfamilar with the math concepts required
# This problem required an understanding of permutations which is taught in MATH 0480 which I did not take

class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        memo = {1: [1]}

        def f(n):
            if n in memo:
                return memo[n]
            else:
                odds = f((n+1)//2)
                evens = f(n//2)
                arr = []
                for x in odds:
                    arr.append(2*x-1)
                for x in evens:
                    arr.append(2*x)
                memo[n] = arr
                return arr

        return f(n)