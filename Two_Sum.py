class Solution:
    def twoSum(self, nums, target):

        # There is exactly one solution
        # If the value in the array is above the target value we can skip over it

        # Use tuples to save the current index value in the list
        indexed_nums = [(value, index) for index, value in enumerate(nums)]
            # 'enumerate' returns an iterable that yields pairs of the form (index, value)
            # The 'for' iterates over the pairs of index, value
            # '(value, index)' is a tuple being constructed for each iteration of the loop


        # Sort values of the list
        sorted_indexed_nums = sorted(indexed_nums, key=lambda x: x[0])
            # The 'sorted()' function returns an array in ascending order
            # The 'key=' parameter specifies a custom function to be used to define how the elements should be compared to determine thier sort order
            # The 'lambda x: x[0]' is an anonymous (or lambda) function that takes a single argument x and returns it's first element

        # Create cursors 
        left = 0
        right = len(sorted_indexed_nums) - 1

        # Bring the right cursor left if it is greater than or equal to the target value
        if target >= 0:
            while (sorted_indexed_nums[right][0] > target and right > left):
                right -= 1
        else:
            while (sorted_indexed_nums[left][0] < target and left < right):
                left += 1

        # Begin searching for combination that matches target value
        currentSum = sorted_indexed_nums[left][0] + sorted_indexed_nums[right][0]
        while (currentSum != target):

            # If the current sum is less than the target value, bring the left cursor to the right
            if currentSum < target:
                left += 1
            
            # Otherwise, bring the right cursor to the left
            else:
                right -= 1

            # Find the new current sum of the values at the left and right cursors
            currentSum = sorted_indexed_nums[left][0] + sorted_indexed_nums[right][0]

        # Find the original indexes from the indexes for the sorted_indexed_nums list
        left = sorted_indexed_nums[left][1]
        right = sorted_indexed_nums[right][1]

        # return an array with the left and right cursors which point to values that sum to the target value
        return [left, right]





