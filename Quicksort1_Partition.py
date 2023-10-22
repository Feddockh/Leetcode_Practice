# Hayden Feddock
# Problem from HackerRank
# 2/13/2023

class Solution:
    
    def quickSort(self, arr):
        
        # Determine the value to pivot around
        pivot = arr[0]
        
        # Create an array for the left (lesser), middle (equal), and right (greater) values
        left = []
        middle = []
        right = []
        
        # Go through the arr and categorize the data
        for x in arr:
            if x > pivot:
                right.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                left.append(x)
        
        # Combine the categories into a single array at the end
        return left + middle + right


# Unit Tests
import unittest
class TestSolution(unittest.TestCase):
    def test(self):
        input = [4,5,3,7,2]
        obj = Solution
        self.assertEqual(obj.quickSort(obj, input), [3, 2, 4, 5, 7])

if __name__ == '__main__':
    unittest.main()