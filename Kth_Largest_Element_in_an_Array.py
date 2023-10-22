class Solution:
    def findKthLargest(self, nums, k):

        # Convert k from kth largest element to kth element (from index 0)
        k = len(nums) - k
        
        # Use quickselect method
        def quickselect(nums, k):

            # Check for the base case
            if len(nums) == 1:
                return nums[0]

            # Pick the first element of nums to pivot around
            p = nums[0]

            # Create subarrays for the left, middle, and right
            left = []
            middle = []
            right = []

            # Iterate through nums and divide the values into thier categories
            for i in range(len(nums)):
                if nums[i] < p:
                    left.append(nums[i])
                elif nums[i] == p:
                    middle.append(nums[i])
                else:
                    right.append(nums[i])

            # Determine which subarray our kth element is within
            if k < len(left):
                return quickselect(left, k)
            elif k < len(left) + len(middle):
                return middle[0]
            else:
                return quickselect(right, k - (len(left) + len(middle)))
        
        return quickselect(nums, k)