class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if the total number of elements matches m * n
        if len(original) != m * n:
            return []  # Return an empty list if it's impossible
        
        # Initialize the 2D array
        result = []
        
        # Fill the 2D array
        for i in range(m):
            # Each row will take a slice of n elements from original
            row = original[i * n:(i + 1) * n]
            result.append(row)
        
        return result
