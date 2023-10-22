class Solution:
    def maxArea(self, height):

        l = 0 # Left pointer
        r = len(height) - 1 # Right pointer

        # Variable to keep trakc of the max water held
        maxWater = 0

        # Function to return the water contained between the two lines
        def waterContained(leftLine, rightLine, distance):

            # Water held is limited by the shorter line
            minLine = min(leftLine, rightLine)

            # return the area of the water
            return minLine * distance

        # Loop until left and right cursors meet
        while(l < r):
            
            # Find the water between the lines and compare to the max value
            maxWater = max(maxWater, waterContained(height[l], height[r], r-l))

            # If the left line is shorter than (or equal to) the right, set the left cursor to the next tallest from the left
            if height[l] <= height[r]:

                # Set cursor for the new left pointer
                l2 = l

                # Find new left pointer by incrementing towards the right cursor until it finds a line taller than the current one it points to
                while (height[l2] <= height[l] and l2 < r):
                    l2 += 1

                # Set the new cursor value for the left cursor
                l = l2
            
            # If the left line is taller than the right, then move the right cursor towards the left
            else:

                # Set the cursor for the new right pointer
                r2 = r

                # Find the new right pointer by incrementing towards the left pointer until it finds a line taller than the current one it points to
                while (height[r2] <= height[r] and r2 > l):
                    r2 -= 1

                # Set the new cursor value for the right cursor
                r = r2

        return maxWater