class Solution:
    def threeSum(self, nums):


        # Function to check if unordered array exists within a list
        def arrayUnique(A, b):
            for i in range(len(A)):
                
                # Convert to sets and check if all values of b are in A[i]
                if set(b) == set(A[i]):
                    return False
            return True


        # Create the output array
        output = []

        # Create a hashmap to hold the values and their positions
        hashmap = {}

        # Fill hashmap with the values from the list
        for i in range(len(nums)):

            # Determine the key for the hashmap (value from nums for finding compliment)
            key = nums[i]

            # Determine the value at the key (index)
            val = i

            hashmap[key] = val
            

        # Choose two values using loops
        for i in range(len(nums)-2):

            # Modify the range to only visit combinations that haven't been visited yet
            for j in range(i+1, len(nums)-1):

                # Get the current sum of the two values
                currentSum = nums[i] + nums[j]

                # Find the compliment based on the current sum
                compliment = 0 - currentSum

                # Check the hashmap for the compliment
                if compliment in hashmap and hashmap[compliment] > i and hashmap[compliment] > j:

                    # Create array for triplet
                    triplet = [nums[i], nums[j], compliment]

                    # Check if the product exists in the checkedVals hashmap
                    if arrayUnique(output, triplet):

                        # Add the triplet to the current output
                        output.append(triplet)
                
        return output

        

