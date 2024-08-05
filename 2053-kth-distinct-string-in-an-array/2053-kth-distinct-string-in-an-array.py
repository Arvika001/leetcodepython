class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Count occurrences of each string
        count = Counter(arr)
        
        # Collect distinct strings
        distinct_strings = [string for string in arr if count[string] == 1]
        
        # Return the kth distinct string, if it exists
        if k <= len(distinct_strings):
            return distinct_strings[k - 1]  # k is 1-indexed
        else:
            return ""  # Not enough distinct strings
