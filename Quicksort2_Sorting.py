# Hayden Feddock
# Problem from HackerRank
# 2/13/2023

class Solution:
    
    def quicksort(self, arr):
        
        # Check for base case
        if len(arr) <= 1:
            return arr
        
        # If not in the base case, create the left, middle, and right lists
        left = []
        middle = []
        right = []
        
        # Determine the pivot value
        pivot = arr[0]
        
        # Iterate through the array and sort elements into categories
        for x in arr:
            if x > pivot:
                right.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                left.append(x)
                
        # Recursively call the function on the left and right subarrays
        left = self.quicksort(self, left)
        right = self.quicksort(self, right)
        
        return left + middle + right



# Unit Tests
import unittest
class TestSolution(unittest.TestCase):
    def test(self):
        input = [5,8,1,3,7,9,2]
        obj = Solution
        self.assertEqual(obj.quicksort(obj, input), [1,2,3,5,7,8,9])

if __name__ == '__main__':
    unittest.main()