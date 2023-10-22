class Solution:
    def smallestTrimmedNumbers(self, nums, queries):

        # Output smallest num after trimming
        output = []

        # For each query in queries
        for query in queries:

            # Create a new nums array of the trimmed nums with the index of its position
            trimmed_nums = []
            for i in range(len(nums)):
                num = nums[i]
                trim = query[1]
                rightmost_digits = num[-trim:]
                trimmed_nums.append([rightmost_digits, i])
            
            # Convert all of the strings to ints
            sorted_nums = list(sorted(trimmed_nums, key=lambda x: int(x[0])))

            # Add the index of the kth smallest value to output
            k = query[0]
            output.append(sorted_nums[k - 1][1])

        return output