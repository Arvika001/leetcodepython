class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)  # Calculates the number of rows
        n = len(colSum)  # Calculates the umber of columns
        
        # Initialize the matrix with zeros
        matrix = [[0] * n for _ in range(m)]
        
        # Initialize pointers for rows and columns
        i, j = 0, 0
        
        # Fill the matrix based on rowSum and colSum
        while i < m and j < n:
            
            # Assign the minimum of the current rowSum and colSum
            matrix[i][j] = min(rowSum[i], colSum[j])
            
            # Update the rowSum and colSum
            rowSum[i] -= matrix[i][j]
            colSum[j] -= matrix[i][j]
            
            # Move to the next row if the current rowSum is 0
            if rowSum[i] == 0:
                i += 1
            # Move to the next column if the current colSum is 0
            if colSum[j] == 0:
                j += 1
        
        return matrix       