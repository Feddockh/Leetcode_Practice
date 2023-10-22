class Solution:
    def findPeakGrid(self, mat):

        # Determine the rows and columns of the matrix
        rows = len(mat)
        cols = len(mat[0])

        # Keep track of checked squares
        checkedSquares = {}

        # Keep track of peaks
        peak = []

        # Check squares recursively
        def checkPeak(mat, i, j, checkedSquares):
            
            # Get the current value of the square
            currentVal = mat[i][j]

            # Store the square's value and it's location to a hashmap for later
            checkedSquares[(i, j)] = currentVal

            # Get all the surrounding values if they exist

            # Get the value of the left square if it exists
            if j-1 >= 0:
                leftVal = mat[i][j-1]
            else:
                leftVal = -1

            # Get the value of the top square if it exists
            if i-1 >= 0:
                topVal = mat[i-1][j]
            else:
                topVal = -1

            # Get the value of the right square if it exists
            if j+1 < len(mat[i]):
                rightVal = mat[i][j+1]
            else:
                rightVal = -1

            # Get the value of the bottom square if it exists
            if i+1 < len(mat):
                bottomVal = mat[i+1][j]
            else:
                bottomVal = -1
            
            # Compare the values of the surrounding squares to that of the current square and the coordinated to the checked squares
            # Depth-first recursive search for the peak value

            # Check the left square if it has a value greater than the current square and has not been checked yet
            if currentVal < leftVal and (i, j-1) not in checkedSquares:
                peak = checkPeak(mat, i, j-1, checkedSquares)

            # Check the top square if it has a value greater than the current square and has not been checked yet
            elif currentVal < topVal and (i-1,j) not in checkedSquares:
                peak = checkPeak(mat, i-1, j, checkedSquares)

            # Check the right square if it has a value greater than the current square and has not been checked yet
            elif currentVal < rightVal and (i,j+1) not in checkedSquares:
                peak = checkPeak(mat, i, j+1, checkedSquares)

            # Check the bottom square if it has a value greater than the current square and has not been checked yet
            elif currentVal < bottomVal and (i+1,j) not in checkedSquares:
                peak = checkPeak(mat, i+1, j, checkedSquares)

            # If there are no squares greater than the current one, then return the coordinates as a peak
            else:
                peak = [i, j]
            
            return peak
        
        # Call the recursive function to find the peak
        return checkPeak(mat, 0, 0, checkedSquares)





