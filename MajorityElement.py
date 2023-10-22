"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

# My solution
class Solution:
    def majorityElement(self, nums):
        majorityCount = 0
        for i in range(len(nums)): # Iterates through each element in the array
            elementCount = 0
            for j in range(len(nums)): # Iterates through each element for each element in the array
                if i == j: # If the loops are on the same index, then skip
                    continue
                elif nums[i] == nums[j]: # If the elements at each index are equal, then add to the total element count
                    elementCount += 1
            majorityCount = max(majorityCount, elementCount) # Check if the most recent element count or the majority is larger
# Time complexity O(n^2)
# Space complexity O(1)
            

# Approach 1: Brute Force
class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums: # Iterates through elements of the array
            count = sum(1 for elem in nums if elem == num) # Iterates through the list for each element and records the number of occurances
            if count > majority_count: # If the count exceeds [n / 2], then return that value
                return num
# Time complexity O(n^2)
# Space complexity O(1)


# Approach 2: HashMap
import collections
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums) # Create a hashmap that maps elements to counts in order to count occurances in linear time
        return max(counts.keys(), key=counts.get) # Return the key with the maximum value
# Time complexity O(n)
# Space complexity O(n)


# Approach 3:  Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for num in nums: # Iterate through the list
            if (count == 0): # If the tally is zero, then set a new candidate based on the next value
                candidate = num
            count += (1 if num == candidate else -1) # If the num matches the candidate vote +1, else vote -1
        return candidate
# Time complexity O(n)
# Space complexity O(1)



# Unit Tests
import unittest
class TestSolution(unittest.TestCase):
    def test1(self):
        input = [3, 2, 3]
        obj = Solution
        self.assertEqual(Solution.majorityElement(obj, input), 3)
        
    def test2(self):
        input = [2, 2, 1, 1, 1, 2, 2]
        obj = Solution
        self.assertEqual(Solution.majorityElement(obj, input), 2)

if __name__ == '__main__':
    unittest.main()