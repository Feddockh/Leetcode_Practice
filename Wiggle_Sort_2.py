class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        # Sort the nums list
        nums.sort()
        
        # Create cursor for midpoint
        # Round up because if list length is odd, the lower list needs to be large enough to sandwich all of the upper values
        mid = math.ceil(len(nums) / 2)

        # Create an FIFO queues for the upper and lower values
        upper = nums[mid:]
        lower = nums[:mid]
        
        # Iterate through nums and pop values from the queues until they are both empty (sandwich upper values with lower ones)
        i = 0
        while(i < len(nums)):

            if (len(lower) > 0):
                nums[i] = lower.pop()
                i += 1

            if (len(upper) > 0):
                nums[i] = upper.pop()
                i += 1