# Hayden Feddock

class Solution:
    def maxSubArray(self, nums):

        memo = {}

        maxVal = -math.inf

        # Search nums list from back to front
        for i in reversed(range(len(nums))):

            # Search the nums subarray
            for j in range(i, len(nums)):

                # Create the subarray
                subarray = nums[i:j+1]

                # Calculate the sum
                count = subarray[0]
                if (i + 1, j) in memo:

                    # Use the pre-calculated sum
                    count += memo[(i + 1, j)]
                else:

                    # If not already calculated, calculate the sum
                    count += sum(subarray[1:])
                    
                    # Store the calculated sum to memory
                    memo[(i, j)] = count
                    
                # Find the maximum
                maxVal = max(maxVal, count)

        return maxVal