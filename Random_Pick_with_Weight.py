class Solution:

        def __init__(self, w):
            self.w = w # Store value of w

        def pickIndex(self):
            return random.choices(range(len(self.w)), weights=self.w)[0] # Use random choices function to randomly pick an index in the range and return it with the weights