class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []  # Initialize the results list
        
        def backtrack(start: int, path: List[int], remaining: int):
            if remaining == 0:  # Base case: if remaining target is 0
                results.append(path[:])  # Add a copy of the current path to results
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:  # If the candidate exceeds remaining, stop
                    break
                
                path.append(candidates[i])  # Include the candidate in the current path
                backtrack(i, path, remaining - candidates[i])  # Recur with updated remaining
                path.pop()  # Backtrack: remove the last added candidate
        
        candidates.sort()  # Optional: sort candidates to facilitate early stopping
        backtrack(0, [], target)  # Start backtracking from index 0
        return results  # Return the list of valid combinations
        