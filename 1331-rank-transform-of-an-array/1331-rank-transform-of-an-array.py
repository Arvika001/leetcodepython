class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: Create a sorted list of unique elements
        unique_sorted = sorted(set(arr))
        
        # Step 2: Create a mapping from element to its rank
        rank_map = {value: rank + 1 for rank, value in enumerate(unique_sorted)}
        
        # Step 3: Replace each element in arr with its rank
        return [rank_map[num] for num in arr]
