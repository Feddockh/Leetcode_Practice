class Solution:
    def findPeakElement(self, nums):

        # Determine the left and right cursors
        left = 0
        right = len(nums) - 1

        # Keep track of the maxVal and it's index
        maxVal = 0
        index = 0

        # Use recursion to break down array with binary search tree
        def getMax(nums, left, right):

            # Base case with one value left
            if left == right:
                maxVal = nums[left]
                index = left
                return [maxVal, index]

            # Base case with two values left
            if left + 1 >= right:
                
                # Set the maxVal and it's index to the larger value and its index
                if nums[left] >= nums[right]:
                    maxVal = nums[left]
                    index = left
                else:
                    maxVal = nums[right]
                    index = right
                
                # Return the maxVal and it's index
                return [maxVal, index]

            # Find the midpoint
            mid = (right - left) // 2 + left

            # Otherwise split array and call recursively
            maxVal_left, index_left = getMax(nums, left, mid)
            maxVal_right, index_right = getMax(nums, mid + 1, right)

            # Compare left and right maxes
            if maxVal_left >= maxVal_right:
                maxVal = maxVal_left
                index = index_left
            else:
                maxVal = maxVal_right
                index = index_right

            return [maxVal, index]

        # Call recursive function
        maxVal, index = getMax(nums, left, right)

        return index




            
