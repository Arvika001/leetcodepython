class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # Directions array for moving up, down, left, and right
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        # DFS method to explore the grid and mark visited cells
        def numberOfIslandsDFS(matrix, i, j):
            rows = len(matrix)
            cols = len(matrix[0])
            
            # Check for out of bounds or already visited
            if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] == 1:
                return
            
            matrix[i][j] = 1  # Mark the cell as visited
            
            # Explore all four directions
            for dir in directions:
                new_i = i + dir[0]
                new_j = j + dir[1]
                numberOfIslandsDFS(matrix, new_i, new_j)

        rows = len(grid)
        cols = len(grid[0])
        regions = 0

        # Create a 3x3 expanded grid to handle slashes
        matrix = [[0] * (cols * 3) for _ in range(rows * 3)]

        # Populate the matrix based on '/' and '\\' in the original grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '/':
                    matrix[i * 3][j * 3 + 2] = 1
                    matrix[i * 3 + 1][j * 3 + 1] = 1
                    matrix[i * 3 + 2][j * 3] = 1
                elif grid[i][j] == '\\':
                    matrix[i * 3][j * 3] = 1
                    matrix[i * 3 + 1][j * 3 + 1] = 1
                    matrix[i * 3 + 2][j * 3 + 2] = 1

        # Apply DFS to count the regions
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:  # If the cell is not visited
                    numberOfIslandsDFS(matrix, i, j)
                    regions += 1  # Increment the region count

        return regions
