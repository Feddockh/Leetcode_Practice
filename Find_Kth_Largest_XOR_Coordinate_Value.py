class Solution:
    def kthLargestValue(self, matrix, k):

        def precompute_xor_sum(matrix):

            # Get the rows and cols
            rows, cols = len(matrix), len(matrix[0])

            # Create the prefix matrix
            prefix = [[0] * cols for _ in range(rows)]

            # Calculate the prefix sum array
            for i in range(rows):
                for j in range(cols):
                    if i == 0 and j == 0:
                        prefix[i][j] = matrix[i][j]
                    elif i == 0:
                        prefix[i][j] = prefix[i][j-1] ^ matrix[i][j]
                    elif j == 0:
                        prefix[i][j] = prefix[i-1][j] ^ matrix[i][j]
                    else:
                        prefix[i][j] = prefix[i-1][j] ^ prefix[i][j-1] ^ prefix[i-1][j-1] ^ matrix[i][j]
            return prefix
        
        def find_kth_largest_value(matrix, k):

            # Add all values to a sorted list
            sorted_list = []
            for row in matrix:
                for val in row:
                    sorted_list.append(val)

            # Sort list from largest to smallest values
            sorted_list.sort(reverse=True)
            
            # Return k largest value
            return sorted_list[k - 1]

        prefix = precompute_xor_sum(matrix)

        return find_kth_largest_value(prefix, k)