# I very much struggled with this one, so I did search around online for help
# I did spend hours trying to figure it out to no avail. A large portion of this code was pulled from the leet code solutions. I do not take credit for it, but I included it to display my effort in understanding the problem's solution.
# I commented everything to display my understanding

class Solution:
    def countSmaller(self, nums):

        # Get the length of the vector
        n = len(nums)

        # Assign numbers to each of the values in the object
        arr = [[v, i] for i, v in enumerate(nums)]

        # Allocate space for the resulting vector
        result = [0] * n

        # sort from smallest to largest values
        def merge_sort(arr, left, right):
            
            # Base case
            if right - left <= 1:
                return

            # Define the midpoint index using floor division
            mid = (left + right) // 2

            # Recursively call merge sort the left subarray
            merge_sort(arr, left, mid)

            # Recursively call merge sort the right subarray
            merge_sort(arr, mid, right)

            # Once everything has been seperated, call the merge function to bring it back together
            merge(arr, left, right, mid)

        # Combine the left and right subarrays into an ordered array
        def merge(arr, left, right, mid):
            
            # Indexes for left and right arrays
            i = left
            j = mid

            # Use temp to temporarily store sorted array
            temp = []

            # If both cursors haven't reached the ends of their subarrays
            while i < mid and j < right:

                # If the value from the left subarray is lower than the value from the right, move it to the temp array and record the switch in the result array, otherwise just move it to the temp array
                if arr[i][0] <= arr[j][0]:
                    result[arr[i][1]] += j - mid
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1

            # Fill the rest of the temp array and count the switch if the right subarray was completed
            while i < mid:
                result[arr[i][1]] += j - mid
                temp.append(arr[i])
                i += 1

            # Transfer the rest of the right subarray to the temp subarray if the left was completed
            while j < right:
                temp.append(arr[j])
                j += 1

            # Copy data from the temp array into the array
            for i in range(left, right):
                arr[i] = temp[i - left]

        merge_sort(arr, 0, n)

        return result