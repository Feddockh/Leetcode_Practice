# Hayden Feddock
# Problem from HackerRank
# 2/13/2023

class Solution:

    def findMedian(arr):
        
        # Use the sort function to sort the list in place
        arr.sort()
        
        # Find the median
        median = arr[len(arr) // 2]

        return median
    
# Unit Tests
import unittest
class TestSolution(unittest.TestCase):
    def test(self):
        input = [0,1,2,4,6,5,3]
        obj = Solution
        self.assertEqual(obj.findMedian(input), 3)

if __name__ == '__main__':
    unittest.main()