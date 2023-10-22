# Hayden Feddock
# Problem from HackerRank
# 2/13/2023

class Solution:
    
    def quicksort(self, arr):
        
        # Check for base case
        if len(arr) <= 1:
            return arr
        
        # Designate the pivot element as the last element in the array
        pivot = arr[len(arr) - 1]
        
        # Create a cursor to keep track of the divide between elements lesser and greater than the pivot value
        split = 0
        
        # Loop through the elements of the array
        for i in range(len(arr) - 1):
        
           
           # If the elements are less than or equal to the pivot value
           if (arr[i] <= pivot):
               
               # If the i cursor is not just in front of the split, and the element is less than the pivot, swap the value that cursor i points to and the value at the split
               if (i >= split + 1):
                   temp = arr[split]
                   arr[split] = arr[i]
                   arr[i] = temp
                   
               # Increment the split value
               split += 1
                   
                   
        # At the end, swap the pivot value at the back of the list into it's proper place
        arr[len(arr) - 1] = arr[split]
        arr[split] = pivot
        
        # Recursively call the function to sort the left and right subarrays
        return self.quicksort(self, arr[:split]) + self.quicksort(self, arr[split:])


# Unit Tests
import unittest
class TestSolution(unittest.TestCase):
    def test(self):
        input = [5,8,1,3,7,9,2]
        obj = Solution
        self.assertEqual(obj.quicksort(obj, input), [1,2,3,5,7,8,9])
        
    def test2(self):
        input = [1,3,9,8,2,7,5]
        obj = Solution
        self.assertEqual(obj.quicksort(obj, input), [1,2,3,5,7,8,9])

if __name__ == '__main__':
    unittest.main()
               
        
        
        