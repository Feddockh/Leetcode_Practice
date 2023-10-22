# Hayden Feddock
# Problem from HackerRank
# 2/13/2023

class Solution:
    
    def insertionSort(self, arr):
        
        # Loop array from front to back
        for i in range(len(arr)):
            
            # Loop through array from front to back
            for j in range(len(arr)):
                
                # Stop when element j is greater than of equal to element i
                if arr[j] >= arr[i]:
                    
                    # If the cursor i is at the same point as j
                    if i == j:
                        break
                    
                    # If the cursor i is further than cursor j
                    elif i > j:
                        
                        # Insert element i at space j
                        arr.insert(j, arr[i])
                        
                        # Remove the new index of the ith element (i + 1)
                        arr.pop(i + 1)
                    
                    # If the cursor i is behind cursor j
                    else:
                    
                        # Insert element i at space j
                        arr.insert(j, arr[i])
                        
                        # Remove the ith element
                        arr.pop(i)
                        
        return arr

                   
        


# Unit Tests
import unittest
class TestSolution(unittest.TestCase):
    def test(self):
        input = [2,1,3,1,2]
        obj = Solution
        self.assertEqual(obj.insertionSort(obj, input), [1,1,2,2,3])

if __name__ == '__main__':
    unittest.main()